import os
import sys

from loguru import logger

from Common.Config import config

LOG_IDENTIFIER = "system"


def get_logger(config):
    sys_logger = logger.bind()
    sys_logger.remove()

    # Define log file path unique to this instance
    log_path = os.path.join(config.app_data_dir, "runs", "run_{time:YYYYMMDD}.log")
    sys_logger.add(
        log_path,
        rotation="1 day",
        level="INFO",
        format=_level_format,
    )

    sys_logger.add(
        sys.stdout,
        colorize=True,
        format=_level_format,
        level="INFO",
    )
    sys_logger.log("INFO", "------------- New Program Run -------------")
    return sys_logger


def _level_format(record: dict) -> str:
    if "label" not in record["extra"]:
        return (
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{"
            "level: <3}</level> | :  <level>{"
            "message}</level>\n"
        )

    # the message from Recorder class
    label = record["extra"]["label"]
    return (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{"
        "level: <3}</level> | : [<level>{label}</level>] <level>{"
        "message}</level>\n"
    ).replace("{label}", label)  # 用格式化后的 label 替换模板中的占位符


sys_logger = get_logger(config)
