from http.client import HTTPException

from main.dao.base_dao import BaseDao
from main.models.user import User
from main.utils.singleton import singleton


@singleton
class UserDao(BaseDao):

    def get_user_by_id(self, id) -> User:
        """
        Get user by id
        :param id:
        """
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT id, name, email FROM user WHERE id = %s", (id,))
            user_data = cursor.fetchone()
            if user_data is None:
                raise HTTPException(status_code=404, detail="User not found")
            return User(**user_data)

    def get_all_users(self) -> list:
        """
        Get all users
        """
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT id, name, email FROM user")

            user_list = []
            for row in cursor.fetchall():
                user = User(**row)
                user_list.append(user)
            self.conn.commit()
            return user_list
