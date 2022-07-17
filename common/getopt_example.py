import getopt
import sys

from loguru import logger

if __name__ == '__main__':
    """
    定义命令行需要传入的参数
    """
    max_workers = 8
    task_num_batch = 2000
    start = 1
    end = 1000
    table_name = "clob_dw_us.ads_m3_report_before_offline_logic"
    blob_path = "m3_offline_logic"

    """
    从命令行读取参数
    """
    try:
        opts, args = getopt.getopt(sys.argv[1:], "t:w:n:b:s:e",
                                   ["task_num_batch=",
                                    "max_workers=",
                                    "table_name=",
                                    "blob_path=",
                                    "start=",
                                    "end="])
    except getopt.GetoptError as err:
        logger.error(str(err))

    for opt, arg in opts:
        if opt in ['-w', "--max_workers"]:
            # 从命令行读取的参数默认是str类型，这里用`int()`函数将它转化为int类型
            max_workers = int(arg)
        elif opt in ['-t', "--task_num_batch"]:
            task_num_batch = int(arg)
        elif opt in ['-n', "--table_name"]:
            table_name = arg
        elif opt in ['-b', "--blob_path"]:
            blob_path = arg
        elif opt in ['-s', "--start"]:
            start = int(arg)
        elif opt in ['-e', "--end"]:
            end = int(arg)

    """
    打印从命令行读取的参数
    """
    logger.info("worker_num:{}, task_num_batch:{}, table_name:{}, blob_path:{}, start:{}, end:{}"
                .format(max_workers, task_num_batch, table_name, blob_path, start, end))
