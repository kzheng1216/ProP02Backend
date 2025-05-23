# 使用官方 Ubuntu 22.04 作为基础镜像
FROM ubuntu:22.04

# 设置环境变量
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.6.1 \
    APP_HOME=/app

# 设置工作目录
WORKDIR $APP_HOME

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.10 \
    python3.10-dev \
    python3-pip \
    python3-venv \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 安装 Poetry
RUN pip3 install "poetry==$POETRY_VERSION"

# 配置 Poetry 使用虚拟环境
RUN poetry config virtualenvs.create false

# 复制项目依赖文件
COPY pyproject.toml poetry.lock ./

# 安装项目依赖
RUN poetry install --no-dev --no-interaction --no-ansi

# 复制项目文件
COPY . .

# 暴露应用端口
EXPOSE 9882

# 运行 Uvicorn 服务器
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9882"]