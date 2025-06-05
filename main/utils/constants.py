from enum import Enum


class DB_INFO:
    HOST = "106.15.33.153"
    PORT = 3306
    USERNAME = "mysql"
    PASSWORD = "Zaq1@wsx"
    DATABASE = "mydb02_dev"
    CHARSET = "utf8mb4"


JWT_SECRET = "abcd1234"
ALGORITHM = "HS512"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

T_USERNAME = "user123"
T_PASSWORD = "pass123"

AUTH_SALT = b"$2b$12$abcdefghijklmnopqrstuv"

REDIS_CONFIG = {
    'host': '106.15.33.153',
    'port': 6379,
    'db': 0,
    'username': 'mystic',
    'password': 'Zaq1@wsx'
}
