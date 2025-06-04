import pymysql
from main.utils.constants import DB_INFO

conn = pymysql.connect(
    host=DB_INFO.HOST,
    user=DB_INFO.USERNAME,
    password=DB_INFO.PASSWORD,
    db=DB_INFO.DATABASE,
    charset=DB_INFO.CHARSET,
    cursorclass=pymysql.cursors.DictCursor
)

class DBConnection:
    def __init__(self):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            # 没有异常，提交事务
            self.conn.commit()
        else:
            # 发生异常，回滚事务
            self.conn.rollback()
        self.cursor.close()    

