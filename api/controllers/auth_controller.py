from typing import Any

from api.schemas.auth_schema import LoginDTO
from dal.repositories.auth_repository import AuthRepository


class AuthController():
    def __init__(self):
        self.repo = AuthRepository()

    def match_login(self, payload: dict[str, Any]):
        if not payload:
            raise ValueError("Payload invalid")

        login_data = LoginDTO(**payload)
        return self.repo.match(login_data.email, login_data.mot_de_passe)
