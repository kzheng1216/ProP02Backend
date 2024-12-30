from fastapi import FastAPI
from main.controllers import api_router


def create_app():
    my_app = FastAPI()
    register_router(my_app)
    return my_app


def register_router(my_app: FastAPI):
    my_app.include_router(api_router)


app = create_app()

# Start up with cmd: uvicorn app:app --port 9882
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='app:app', host="0.0.0.0", port=9882, limit_concurrency=50, reload=True, debug=True)