from fastapi import APIRouter
from main.controllers import test_controller, user_controller, auth_controller

api_router = APIRouter()

api_router.include_router(test_controller.router, prefix="", tags=['Test Controller'])
api_router.include_router(user_controller.router, prefix="", tags=['User Controller'])
api_router.include_router(auth_controller.router, prefix="", tags=['Auth Controller'])