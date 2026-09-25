from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.jwt import create_access_token
from app.core.security import (
    hash_password,
    verify_password,
)
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate


class AuthService:

    def __init__(self):
        self.repository = UserRepository()

    def register(
        self,
        db: Session,
        data: UserCreate
    ) -> User:

        existing_user = self.repository.get_by_email(
            db,
            data.email
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        hashed_password = hash_password(
            data.password
        )

        user = User(
            name=data.name,
            email=data.email,
            password_hash=hashed_password,
            role=data.role,
            is_active=True
        )

        return self.repository.create(
            db,
            user
        )

    def login(
        self,
        db: Session,
        email: str,
        password: str
    ) -> str:

        user = self.repository.get_by_email(
            db,
            email
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        if not verify_password(
            password,
            user.password_hash
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User account is inactive"
            )

        return create_access_token(
            user.id
        )