import sqlite3


def create_sql_table(database_path="database/sqlite.db"):
    """
    初始化表
    :param database_path: 数据库文件路径
    """
    # 连接 SQLite 数据库
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # 创建向量库信息表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vdb_info (
            name TEXT PRIMARY KEY,
            type TEXT NOT NULL,
            embedding_model_name TEXT NOT NULL,
            parameters JSON,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')

    # 创建文件表（使用哈希值作为主键）
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS files (
            file_hash TEXT PRIMARY KEY,
            filename TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')

    # 创建文件与向量库的关联表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS file_vdb (
            file_hash TEXT,
            vdb_name TEXT,
            PRIMARY KEY (file_hash, vdb_name),
            FOREIGN KEY (file_hash) REFERENCES files(file_hash) ON DELETE CASCADE,
            FOREIGN KEY (vdb_name) REFERENCES vdb_info(name) ON DELETE CASCADE
        );
    ''')

    # 提交更改
    conn.commit()

    # 关闭游标和连接
    cursor.close()
    conn.close()
