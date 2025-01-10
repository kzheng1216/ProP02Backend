from main.dao.user_dao import UserDao


class UserService:

    def get_user_by_id(self, id: int):
        return UserDao().get_user_by_id(id)

    def get_all_users(self):
        return UserDao().get_all_users()
