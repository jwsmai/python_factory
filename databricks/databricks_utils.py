import os

from databricks import sql
from loguru import logger


@logger.catch
def get_result_from_databricks():
    """
    get result from databricks use sql
    :return:
    """
    connection = sql.connect(
        server_hostname=os.getenv('DATABRICKS_SERVER_HOSTNAME'),
        http_path=os.getenv('DATABRICKS_HTTP_PATH'),
        access_token=os.getenv('DATABRICKS_TOKEN'))

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM RANGE(10)')
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    connection.close()


get_result_from_databricks()
