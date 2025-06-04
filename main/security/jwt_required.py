from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
from functools import wraps
import jwt
import fnmatch
from main.utils.constants import JWT_SECRET, ALGORITHM, USER_API_PERMISSIONS
import datetime


def generate_token(username="admin"):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'sub': username,
        'name': username
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)
    print("Token generated: ", token)
    return token


def jwt_required():
    def decorator(func):
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
                
                if username in USER_API_PERMISSIONS:
                    is_api_authorized = False
                    api_rules = USER_API_PERMISSIONS[username]
                    for api_rule in api_rules:
                        if fnmatch.fnmatch(api_url, api_rule):
                            print(f'User has permission to access this resource. {api_url}|{api_rules}')
                            is_api_authorized = True
                            break
                    if not is_api_authorized:
                        print(f'User does not have permission to access this resource. {api_url}|{api_rules}')
                        raise HTTPException(status_code=403, detail="User does not have permission to access this resource")               
                else:   
                    raise HTTPException( status_code=403, detail="User does not have permission to access this resource")
                
            except jwt.ExpiredSignatureError:
                raise HTTPException(status_code=401, detail="Token expired")
            except jwt.InvalidTokenError:
                raise HTTPException(status_code=401, detail="Invalid token")

            return await func(request, *args, **kwargs)
        return wrapper
    return decorator
