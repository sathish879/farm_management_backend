from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.user import UserController
from app.core.dependencies import get_db
from app.core.roles import require_admin
from app.schemas.user import UserCreate, UserResponse


router = APIRouter(
    prefix="/users",
    tags=["User Management"]
)

controller = UserController()


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_admin)]
)
def create_user(
    data: UserCreate,
    db: Session = Depends(get_db)
):
    """Create a new user. Only ADMIN can create users."""

    return controller.create_user(
        db,
        data
    )