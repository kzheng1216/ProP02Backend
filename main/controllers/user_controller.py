from fastapi import APIRouter, HTTPException, Request
from main.security.jwt_required import jwt_required
from main.services.user_service import UserService

router = APIRouter()


@router.get("/api/user/{id}")
@jwt_required()
async def get_user(request: Request, id: int):
    return UserService().get_user_by_id(id)


@router.get("/api/users")
@jwt_required()
async def get_all_users(request: Request):
    return UserService().get_all_users()
