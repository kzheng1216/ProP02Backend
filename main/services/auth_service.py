from main.utils.constants import T_USERNAME, T_PASSWORD


class AuthService:

    @staticmethod
    def validate_user(username, password):
        if username == T_USERNAME and password == T_PASSWORD:
            return True
        return False
