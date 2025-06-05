from fastapi import APIRouter, HTTPException, Request
from main.security.auth_required import AuthRequired
from main.services.user_service import UserService

router = APIRouter()


@router.get("/api/user/{id}")
@AuthRequired()
async def get_user(request: Request, id: int):
    return UserService().get_user_by_id(id).dict(exclude_none=True)


@router.get("/api/users")
@AuthRequired()
async def get_all_users(request: Request):
    return UserService().get_all_users()
