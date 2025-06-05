import datetime
from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
from functools import wraps
import jwt
from main.utils.constants import JWT_SECRET, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


class AuthRequired: 
    
    @staticmethod
    def generate_token(username="admin"):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
            'iat': datetime.datetime.utcnow(),
            'sub': username,
            'name': username
        }
        token = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)
        print("Token generated: ", token)
        return token

    def __call__(self, func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Bearer "):
                raise HTTPException(status_code=401, detail="Missing or invalid token")
            token = auth_header.split(" ")[1]
            try:
                payload = jwt.decode(token, JWT_SECRET, algorithms=ALGORITHM)
                username = payload.get('sub')
                api_url = request.url.path
                print("API URL:", api_url)
                
            except jwt.ExpiredSignatureError:
                raise HTTPException(status_code=401, detail="Token expired")
            except jwt.InvalidTokenError:
                raise HTTPException(status_code=401, detail="Invalid token")

            return await func(request, *args, **kwargs)
        return wrapper
