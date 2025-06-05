from main.dao.user_dao import UserDao
from main.utils.constants import T_USERNAME, T_PASSWORD


class AuthService:

    @staticmethod
    def logon(username, password):
        # if username == T_USERNAME and password == T_PASSWORD:
        #     return True
        # return False
        return UserDao().logon(username, password)
    