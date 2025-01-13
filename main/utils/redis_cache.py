import redis
import json
from functools import wraps
from main.utils.constants import REDIS_CONFIG


# 创建Redis连接池
redis_pool = redis.ConnectionPool(**REDIS_CONFIG)


def redis_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # 获取Redis连接
            redis_client = redis.Redis(connection_pool=redis_pool)

            # 执行被装饰函数
            result = func(redis_client, *args, **kwargs)

            # 返回结果
            return result
        except redis.RedisError as e:
            # 处理Redis异常
            print(f"Redis error: {e}")
            return None
        finally:
            # 关闭Redis连接
            redis_client.close()
    return wrapper


@redis_decorator
def read_redis_data(redis_client, key):
    # 从Redis中获取数据
    value = redis_client.get(key)

    # 如果数据存在，将其解码为JSON
    if value:
        return json.loads(value.decode('utf-8'))
    else:
        return None


@redis_decorator
def write_redis_data(redis_client, key, value):
    # 将数据编码为JSON
    json_value = json.dumps(value)

    # 将数据写入Redis
    redis_client.set(key, json_value)


# 写入数据到Redis
write_redis_data("user_2", {"id": 2, "name": "name_2", "email": "email_2"})

# 从Redis中读取数据
print(read_redis_data('user_2'))





