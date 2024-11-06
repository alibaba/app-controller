import argparse
import sys
import threading
import traceback

from Exception.Exception import TaskCancelledException

sys.path.append("Core")

from Common.ChatReposne import Response
from Common.Config import config
from Common.CustomEnum import ResponseStatusEnum
from Common.SysLogger import sys_logger

from Index.EmbedIndexManager import index_manager
from init import init_server, close_server
from AppSupports.SmartVscodeExtension.code.Benchmark.Test.TestManager import TestManager
from Common.Recoder import Recorder
from Database.Models.SessionModel import SessionModel
from Pipeline.ChatPipeline import ChatPipeline
from Pipeline.IntentKnowledgeChatPipeline import IntentKnowledgeAgentChatPipeline
from aiohttp import web
import aiohttp_cors
from Common.Utils import update_model_config, load_local_model_config, remove_model_config
from Common.Context import Context
from Pipeline.KnowledgeChatPipeline import KnowledgeAgentChatPipeline

parser = argparse.ArgumentParser(description="App-Controller Service")
parser.add_argument("--port", "-p", type=int, default=config.SERVER_PORT, help="The port of the service")

session_id_2_pipeline = {}
session_id_2_test_manager = {}
session_id_2_timer = {}


def is_cancelled_pipeline(context: Context):
    if context.session_id not in session_id_2_pipeline:
        return True
    if session_id_2_pipeline[context.session_id].is_task_cancelled:
        return True
    return False


def get_pipeline(context: Context):
    if context.session_id not in session_id_2_pipeline:
        if config.test_mode:
            session_id_2_pipeline[context.session_id] = KnowledgeAgentChatPipeline(config, context)
        else:
            session_id_2_pipeline[context.session_id] = IntentKnowledgeAgentChatPipeline(config, context)
    pipeline = session_id_2_pipeline[context.session_id]
    pipeline.reset()
    return pipeline


def get_test_manager(context: Context):
    if context.session_id not in session_id_2_test_manager:
        session_id_2_test_manager[context.session_id] = TestManager(config, context)
    return session_id_2_test_manager[context.session_id]


def get_timer(context: Context):
    if context.session_id not in session_id_2_timer:
        session_id_2_timer[context.session_id] = threading.Timer(config.session_time_out, handle_time_out, [context])
    return session_id_2_timer[context.session_id]


async def start(request):
    context = Context.from_dict(await request.json())

    # update model config
    update_model_config(context)

    test_manager = get_test_manager(context)
    pipeline = get_pipeline(context)
    timer = get_timer(context)
    print("Start timer")
    timer.start()

    try:
        result: Response = await pipeline.start(context)
        if result.status != ResponseStatusEnum.TASK_QUESTION:
            test_manager.check(result)

        if is_cancelled_pipeline(context):
            clear(context)
            result = Response.get_task_cancelled_response()
    except Exception as e:
        return await _handle_exception(request, context, e)

    # task should be finished immediately when it is a question
    if result.status in {ResponseStatusEnum.TASK_QUESTION, ResponseStatusEnum.TASK_FAILED}:
        await finish(request)
    return web.json_response(result.to_json())


async def handle_api_response(request):
    context = Context.from_dict(await request.json())
    if is_cancelled_pipeline(context):
        clear(context)
        result = Response.get_task_cancelled_response()
    else:
        try:
            pipeline = session_id_2_pipeline[context.session_id]
            test_manager = get_test_manager(context)
            result = await pipeline.handle_api_response(context)
            test_manager.check(result)
            if is_cancelled_pipeline(context):
                clear(context)
                result = Response.get_task_cancelled_response()
        except Exception as e:
            return await _handle_exception(request, context, e)

    if result.status in {ResponseStatusEnum.TASK_FAILED}:
        await finish(request)
    return web.json_response(result.to_json())


async def finish(request):
    """
    1. save data
    2. clear context
    """
    context = Context.from_dict(await request.json())
    get_test_manager(context).task_finished()

    recorder = Recorder(config, context.session_id)
    await recorder.save()

    clear(context)

    return web.json_response({})


async def cancel(request):
    context = Context.from_dict(await request.json())
    if context.session_id in session_id_2_pipeline:
        pipeline: ChatPipeline = session_id_2_pipeline[context.session_id]
        pipeline.stop_task()
    return web.json_response({})


def clear(context: Context):
    if context.session_id in session_id_2_pipeline:
        del session_id_2_pipeline[context.session_id]
    if context.session_id in session_id_2_test_manager:
        del session_id_2_test_manager[context.session_id]
    if context.session_id in session_id_2_timer:
        timer = session_id_2_timer[context.session_id]
        timer.cancel()
        del session_id_2_timer[context.session_id]

    recorder = Recorder(config, context.session_id)
    recorder.close()

    remove_model_config(context)


def handle_time_out(context):
    if context.session_id in session_id_2_test_manager:
        test_manager = get_test_manager(context)
        test_manager.task_failed(f"Time out: {config.session_time_out} seconds")
        test_manager.task_finished()
    clear(context)


async def query_session(request):
    data = await request.json()
    model: SessionModel = await SessionModel.filter(session_id=data["session_id"]).first()
    print(model)
    return web.json_response({"model": model.to_json()})


async def _handle_exception(request, context: Context, e: Exception):
    get_test_manager(context).task_failed()
    await finish(request)

    if isinstance(e, TaskCancelledException):
        return web.json_response(Response.get_task_cancelled_response().to_json())
    else:
        sys_logger.error(f"Unhandled Exception: {e}. Stack Trace: {traceback.format_exc()}")
        return web.json_response(Response.get_exception_response(str(e)).to_json())


def create_app():
    app = web.Application()
    # 添加路由
    app.add_routes([
        web.post('/start', start),
        web.post('/handleApiResponse', handle_api_response),
        web.post('/finish', finish),
        web.post('/cancel', cancel),
        web.post('/query_session', query_session)
    ])
    # 设置 CORS
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })
    for route in list(app.router.routes()):
        cors.add(route)
    # 添加启动和关闭时的钩子
    app.on_startup.append(init_server)
    app.on_cleanup.append(close_server)
    return app


if __name__ == '__main__':
    load_local_model_config("embed_model_config.json")
    index_manager.build_indexes()
    args = parser.parse_args()
    app = create_app()
    web.run_app(app, port=args.port)
