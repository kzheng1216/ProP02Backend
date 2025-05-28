# 使用官方 Python 运行时作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY . .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 容器对外暴露的端口
EXPOSE 9882

# 启动应用
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9882"]
