from fastapi import APIRouter, HTTPException
from main.services.user_service import UserService

router = APIRouter()


@router.get("/api/users")
async def get_all_users():
    return UserService().get_users()
