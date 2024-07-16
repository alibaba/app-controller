import os
import sys

sys.path.append("Core")

from concurrent.futures.thread import ThreadPoolExecutor
from tortoise import Tortoise
from Common.Config import config
import agentscope


async def init_db():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        db_url='sqlite://{}/AppWielder.sqlite3'.format(os.path.join(config.app_data_dir, "UserData")),
        modules={'models': ["Database.Models.SessionModel"]}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


async def init_server(app):
    await init_db()


async def close_server(app):
    await Tortoise.close_connections()


agentscope.init(save_dir="AppSupports/SmartVscodeExtension/runs/Ignore", save_log=False, save_code=False, save_api_invoke=False,
                use_monitor=False)

model_response_thread_pool = ThreadPoolExecutor(max_workers=config.model_response_thread_size)
