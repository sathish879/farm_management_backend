from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.services.user import UserService


class UserController:

    def __init__(self):
        self.service = UserService()

    def create_user(
        self,
        db: Session,
        data: UserCreate
    ):
        """Create a new user through the user service."""

        return self.service.create_user(
            db,
            data
        )