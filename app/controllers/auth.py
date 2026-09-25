from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.services.auth import AuthService


class AuthController:

    def __init__(self):
        self.service = AuthService()

    def register(
        self,
        db: Session,
        data: UserCreate
    ):

        return self.service.register(
            db,
            data
        )

    def login(
        self,
        db: Session,
        email: str,
        password: str
    ):

        token = self.service.login(
            db,
            email,
            password
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }