import pymysql
from main.utils.constants import DB_INFO


class MysqlConnection:
    def get_db_connection(self):
        return pymysql.connect(
            host=DB_INFO.HOST,
            user=DB_INFO.USERNAME,
            password=DB_INFO.PASSWORD,
            db=DB_INFO.DATABASE,
            charset=DB_INFO.CHARSET,
            cursorclass=pymysql.cursors.DictCursor
        )


conn = MysqlConnection().get_db_connection()
