from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.income import IncomeController
from app.core.dependencies import get_db
from app.core.roles import require_authenticated_user
from app.schemas.income import (
    IncomeCreate,
    IncomeUpdate,
    IncomePatch,
    IncomeResponse,
)


router = APIRouter(
    prefix="/income",
    tags=["Income"]
)

controller = IncomeController()


@router.post(
    "/",
    response_model=IncomeResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_authenticated_user)]
)
def create_income(
    data: IncomeCreate,
    db: Session = Depends(get_db)
):
    """Create a new income record."""

    return controller.create(
        db,
        data
    )


@router.get(
    "/",
    response_model=list[IncomeResponse],
    dependencies=[Depends(require_authenticated_user)]
)
def get_income(
    db: Session = Depends(get_db)
):
    """Get all income records."""

    return controller.get_all(db)


@router.get(
    "/{income_id}",
    response_model=IncomeResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def get_income_by_id(
    income_id: int,
    db: Session = Depends(get_db)
):
    """Get an income record by ID."""

    return controller.get_by_id(
        db,
        income_id
    )


@router.put(
    "/{income_id}",
    response_model=IncomeResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def update_income(
    income_id: int,
    data: IncomeUpdate,
    db: Session = Depends(get_db)
):
    """Update an income record completely."""

    return controller.update(
        db,
        income_id,
        data
    )


@router.patch(
    "/{income_id}",
    response_model=IncomeResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def patch_income(
    income_id: int,
    data: IncomePatch,
    db: Session = Depends(get_db)
):
    """Partially update an income record."""

    return controller.patch(
        db,
        income_id,
        data
    )


@router.delete(
    "/{income_id}",
    dependencies=[Depends(require_authenticated_user)]
)
def delete_income(
    income_id: int,
    db: Session = Depends(get_db)
):
    """Delete an income record."""

    return controller.delete(
        db,
        income_id
    )