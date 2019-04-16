# -*-coding:utf-8 -*-

import logging.config
import logging
from Config.ProjVar import *

logging.config.fileConfig(conf_path)
logger = logging.getLogger("example01")


# def debug(message, *args, **kw):
#     """打印debug级别日志的方法"""
#     logger.debug(message, *args, **kw)
#
#
# def warning(message, *args, **kw):
#     """打印warning级别日志的方法"""
#     logger.warning(message, *args, **kw)
#
#
# def info(message, *args, **kw):
#     """打印info级别日志的方法"""
#     logger.info(message)

def debug(message):
    """打印debug级别日志的方法"""
    logger.debug(message)


def warning(message):
    """打印warning级别日志的方法"""
    logger.warning(message)


def info(message):
    """打印info级别日志的方法"""
    logger.info(message)


def error(message):
    """打印error日志的方法"""
    logger.error(message)




if __name__ == "__main__":
    debug("debug:hello")
    warning("waring:hello")
    info("info:hello")
