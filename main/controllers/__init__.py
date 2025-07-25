from fastapi import APIRouter
from main.controllers import test_controller, user_controller, auth_controller, run_testcase_controller, cmd_controller, \
    note_controller

api_router = APIRouter()

api_router.include_router(test_controller.router, prefix="", tags=['Test Controller'])
api_router.include_router(user_controller.router, prefix="", tags=['User Controller'])
api_router.include_router(note_controller.router, prefix="", tags=['Note Controller'])
api_router.include_router(auth_controller.router, prefix="", tags=['Auth Controller'])
api_router.include_router(run_testcase_controller.router, prefix="", tags=['Run Tests Controller'])
api_router.include_router(cmd_controller.router, prefix="", tags=['Run command Controller'])