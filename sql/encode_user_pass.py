import bcrypt

# 原始密码
password = "pass123"

# 固定盐值
AUTH_SALT = b"$2b$12$abcdefghijklmnopqrstuv"

# 哈希密码
hashed_password = bcrypt.hashpw(password.encode(), AUTH_SALT).decode()

# 输出盐和哈希值
print(f"Hashed Password: {hashed_password}")


