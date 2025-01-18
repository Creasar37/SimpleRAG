import sqlite3
from src.logger.logger import logger


def execute_sql(query, database_path="database/sqlite.db", params=None, fetch_results=False):
    """
    执行 SQL 语句的通用函数。

    :param database_path: 数据库文件路径
    :param query: SQL 语句
    :param params: SQL 语句中的参数（默认 None）
    :param fetch_results: 是否返回查询结果（默认 False）
    :return: 如果 fetch_results=True，返回查询结果；否则返回 None
    """
    conn = None
    cursor = None
    try:
        # 连接数据库并启用外键约束
        conn = sqlite3.connect(database_path)
        conn.execute("PRAGMA foreign_keys = ON;")  # 启用外键约束
        cursor = conn.cursor()

        # 执行 SQL 语句
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        # 如果需要返回结果（例如 SELECT 查询）
        if fetch_results:
            results = cursor.fetchall()
            return results

        # 提交非查询操作（如 INSERT、UPDATE、DELETE）
        conn.commit()
    except sqlite3.Error as e:
        logger.error(f"SQL执行错误: {e}\nSQL: {query}\n参数: {params}")
        return None
    finally:
        # 关闭游标和连接
        if cursor:
            cursor.close()
        if conn:
            conn.close()
