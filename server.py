import sys
import argparse
import traceback

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
from Common.Utils import update_model_config, load_model_config
from Common.Context import Context
from Pipeline.KnowledgeChatPipeline import KnowledgeAgentChatPipeline

parser = argparse.ArgumentParser(description="App-Controller Service")
parser.add_argument("--port", "-p", type=int, default=config.SERVER_PORT, help="The port of the service")

session_id_2_pipeline = {}
session_id_2_test_manager = {}


def is_valid_pipeline(context: Context):
    if context.session_id not in session_id_2_pipeline:
        return False

    if not session_id_2_pipeline[context.session_id].is_started:
        return False
    return True


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


async def start(request):
    context = Context.from_dict(await request.json())

    # update model config
    update_model_config(context)

    test_manager = get_test_manager(context)
    pipeline = get_pipeline(context)

    try:
        result: Response = await pipeline.start(context)
        if result.status != ResponseStatusEnum.TASK_QUESTION:
            test_manager.check(result)
    except Exception as e:
        stack_trace = traceback.format_exc()
        sys_logger.error(f"An error occurred: {e}\n\nStack Trace:\n{stack_trace}")
        result = Response.get_exception_response()
        test_manager.task_failed()
        await finish(request)

    # task may be cancelled
    if not is_valid_pipeline(context):
        clear(context)
        result = Response.get_task_cancelled_response()

    # task should be finished immediately when it is a question
    if result.status == ResponseStatusEnum.TASK_QUESTION:
        await finish(request)    
    return web.json_response(result.to_json())


async def handle_api_response(request):
    context = Context.from_dict(await request.json())
    if not is_valid_pipeline(context):
        result = Response.get_task_cancelled_response()
    else:
        pipeline = session_id_2_pipeline[context.session_id]
        test_manager = get_test_manager(context)
        try:
            result = await pipeline.handle_api_response(context)
            test_manager.check(result)
        except Exception as e:
            stack_trace = traceback.format_exc()
            sys_logger.error(f"An error occurred: {e}\n\nStack Trace:\n{stack_trace}")
            result = Response.get_exception_response()
            test_manager.task_failed()
            await finish(request)

    if not is_valid_pipeline(context):
        clear(context)
        result = Response.get_task_cancelled_response()

    return web.json_response(result.to_json())


async def finish(request):
    context = Context.from_dict(await request.json())
    test_manager = get_test_manager(context)
    test_manager.task_finished()

    recorder = Recorder(config, context.session_id)
    await recorder.save()

    clear(context)

    return web.json_response({})


async def cancel(request):
    context = Context.from_dict(await request.json())
    if context.session_id in session_id_2_pipeline:
        pipeline: ChatPipeline = session_id_2_pipeline[context.session_id]
        pipeline.is_started = False
    return web.json_response({})


def clear(context: Context):
    if context.session_id in session_id_2_pipeline:
        del session_id_2_pipeline[context.session_id]
        del session_id_2_test_manager[context.session_id]

    recorder = Recorder(config, context.session_id)
    recorder.close()


async def query_session(request):
    data = await request.json()
    model: SessionModel = await SessionModel.filter(session_id=data["session_id"]).first()
    print(model)
    return web.json_response({"model": model.to_json()})


app = web.Application()
app.add_routes([web.post('/start', start),
                web.post('/handleApiResponse', handle_api_response),
                web.post('/finish', finish),
                web.post('/cancel', cancel),
                web.post('/query_session', query_session)])

# Set up the CORS configuration
cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*",
    )
})

# Apply CORS settings to every route
for route in list(app.router.routes()):
    cors.add(route)

# Set up the database initialization and closing hooks
app.on_startup.append(init_server)
app.on_cleanup.append(close_server)

if __name__ == '__main__':
    load_model_config("embed_model_config.json")
    index_manager.build_indexes()
    args = parser.parse_args()
    web.run_app(app, port=args.port)
