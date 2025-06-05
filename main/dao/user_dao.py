import bcrypt
from http.client import HTTPException
from main.utils.constants import AUTH_SALT
from main.utils.db_conn import DBConnection
from main.dao.base_dao import BaseDao
from main.models.user import User
from main.utils.singleton import singleton


@singleton
class UserDao(BaseDao):
    def logon(self, username: str, password: str) -> bool:
        """
        Check if the user is authenticated
        :param username: Username
        :param password: Password
        :return: True if authenticated, False otherwise
        """
        if not username or not password:
            raise HTTPException(status_code=400, detail="Username and password must be provided")
        
        hashed_password = bcrypt.hashpw(password.encode(), AUTH_SALT).decode()
        
        with DBConnection() as cursor:
            cursor.execute("SELECT password FROM user WHERE name = %s AND password= %s", (username, hashed_password, ))
            result = cursor.fetchone()
            if result is None:
                return False
            return True
        
    def get_user_by_id(self, id) -> User:
        """
        Get user by id
        :param id:
        """
        with DBConnection() as cursor:
            cursor.execute("SELECT id, name, email FROM user WHERE id = %s", (id,))
            user_data = cursor.fetchone()
            if user_data is None:
                raise HTTPException(status_code=404, detail="User not found")
            return User(**user_data)

    def get_all_users(self) -> list:
        """
        Get all users
        """
        with DBConnection() as cursor:
            cursor.execute("SELECT id, name, email FROM user")

            user_list = []
            for row in cursor.fetchall():
                user = User(**row).dict(exclude_none=True)
                user_list.append(user)
            return user_list
