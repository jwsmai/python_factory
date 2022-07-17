from loguru import logger

"""
输出日志到文件
"""
# rotation='00:00' 每天零点创建日志文件，历史日志保留10天
logger.add('log/runtime_{time}.log', rotation='00:00', level="DEBUG", retention='10 days')
logger.debug("this is a debug message to log/runtime.log")

"""
Traceback记录
"""


@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)


my_function(1, -1, 0)
