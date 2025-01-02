from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from main.controllers import api_router


def create_app():
    my_app = FastAPI()
    register_router(my_app)
    register_middleware(my_app)
    return my_app


def register_router(my_app: FastAPI):
    my_app.include_router(api_router)


def register_middleware(my_app: FastAPI):
    my_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 允许所有来源
        allow_credentials=True,
        allow_methods=["*"],  # 允许所有方法
        allow_headers=["*"],  # 允许所有头
    )

app = create_app()

# Start up with cmd: uvicorn app:app --port 9882
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='app:app', host="0.0.0.0", port=9882, limit_concurrency=50, reload=True, debug=True)