from main.models.user import User
from main.utils.db_conn import conn


class UserService:

    @staticmethod
    def get_users():
        with conn.cursor() as cursor:
            sql = "SELECT id, name, email FROM user"
            cursor.execute(sql)
            result = cursor.fetchall()
            return [User(id=user['id'], name=user['name'], email=user['email']) for user in result]
