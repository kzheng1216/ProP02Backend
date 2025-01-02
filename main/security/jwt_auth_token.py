import jwt
import datetime

from main.utils.constants import JWT_SECRET, ALGORITHM


class TokenProvider:

    @staticmethod
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
