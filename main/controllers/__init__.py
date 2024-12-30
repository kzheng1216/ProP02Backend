from fastapi import APIRouter

from main.controllers import test_controller

api_router = APIRouter()

api_router.include_router(test_controller.router, prefix="", tags=['Test Controller'])