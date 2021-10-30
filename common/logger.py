import logging
from logging import config
from os import path

__CON_LOG = path.join(path.dirname(path.dirname(__file__)), r'config\log_config.conf', )
print(__CON_LOG)
logging.config.fileConfig(__CON_LOG)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("selenium").setLevel(logging.WARNING)
logger = logging.getLogger()  # 定义日志采集器
