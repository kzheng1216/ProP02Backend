from main.models.user import User
from main.utils.db_conn import conn


class UserService:
    def get_users(self):
        with conn.cursor() as cursor:
            sql = "SELECT id, name, email FROM user"
            cursor.execute(sql)
            result = cursor.fetchall()
            return [User(id=user['id'], name=user['name'], email=user['email']) for user in result]
