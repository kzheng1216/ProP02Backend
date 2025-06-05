from fastapi import APIRouter, HTTPException
from main.security.auth_required import AuthRequired
from main.models.auth_data import AuthData
from main.services.auth_service import AuthService

router = APIRouter()


@router.post("/auth/login")
async def authenticate_user(login_data: AuthData):

    if AuthService.logon(login_data.username, login_data.password):
        token = AuthRequired.generate_token(login_data.username)
        return {
            "token": token
        }
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
