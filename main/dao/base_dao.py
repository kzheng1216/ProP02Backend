from main.utils.db_conn import conn as db_conn


class BaseDao:
    def __init__(self):
        self.conn = db_conn
