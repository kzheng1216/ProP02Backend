from fastapi import APIRouter, HTTPException
from main.services.user_service import UserService

router = APIRouter()


@router.get("/api/user/{id}")
async def get_user(id: int):
    return UserService().get_user_by_id(id)


@router.get("/api/users")
async def get_all_users():
    return UserService().get_all_users()
