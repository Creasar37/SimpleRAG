import sqlite3

def create_vectors_info_table(database_path="database/sqlite.db"):
    """
    创建 vectors_info 表，如果不存在。
    :param database_path: 数据库文件路径
    """
    # 连接 SQLite 数据库
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # 创建表的 SQL 语句
    create_table_query = """
    CREATE TABLE IF NOT EXISTS vectors_info (
        name TEXT PRIMARY KEY,
        type TEXT NOT NULL,
        embedding_model_name TEXT NOT NULL,
        parameters JSON NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    # 执行 SQL 语句
    cursor.execute(create_table_query)

    # 提交更改
    conn.commit()

    # 关闭游标和连接
    cursor.close()
    conn.close()
