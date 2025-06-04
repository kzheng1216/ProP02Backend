from fastapi import APIRouter, HTTPException
from main.security.jwt_required import generate_token
from main.models.auth_data import AuthData
from main.services.auth_service import AuthService

router = APIRouter()


@router.post("/auth/login")
async def authenticate_user(login_data: AuthData):

    if AuthService.validate_user(login_data.username, login_data.password):
        token = generate_token(login_data.username)
        return {
            "token": token
        }
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
