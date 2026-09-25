from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.jwt import verify_access_token
from app.database import SessionLocal
from app.models.user import User
from app.repositories.user import UserRepository


security = HTTPBearer()
user_repository = UserRepository()


def get_db():
    """
    Create a database session for the request.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """
    Verify the JWT token and return the logged-in user.
    """

    token = credentials.credentials

    user_id = verify_access_token(token)

    user = user_repository.get_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive"
        )

    return user