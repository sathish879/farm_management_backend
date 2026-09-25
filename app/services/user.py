from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def create_user(
        self,
        db: Session,
        data: UserCreate
    ) -> User:
        """Create a new user with a hashed password."""

        existing_user = self.repository.get_by_email(
            db,
            data.email
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        hashed_password = hash_password(data.password)

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