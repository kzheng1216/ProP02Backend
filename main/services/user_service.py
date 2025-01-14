import json

from main.dao.user_dao import UserDao
from main.utils.redis_cache import read_redis_data, write_redis_data
from retry import retry


class UserService:

    @retry(exceptions=Exception, tries=3, delay=2)
    def get_user_by_id(self, id: int):
        user_data_redis = read_redis_data(f"user_{id}")
        if user_data_redis:
            print(f"-->>user_{id} found in redis, data: {user_data_redis}")
            return user_data_redis

        user_data_db = UserDao().get_user_by_id(id)
        if user_data_db:
            print(f"-->>Save user_{id} in redis")
            write_redis_data(f"user_{id}", user_data_db.dict())

        return user_data_db


    def get_all_users(self):
        return UserDao().get_all_users()
