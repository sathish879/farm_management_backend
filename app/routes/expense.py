from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.expense import ExpenseController
from app.core.dependencies import get_db
from app.core.roles import require_authenticated_user
from app.schemas.expense import (
    ExpenseCreate,
    ExpenseUpdate,
    ExpensePatch,
    ExpenseResponse,
)


router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

controller = ExpenseController()


@router.post(
    "/",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_authenticated_user)]
)
def create_expense(
    data: ExpenseCreate,
    db: Session = Depends(get_db)
):
    """Create a new expense."""

    return controller.create(
        db,
        data
    )


@router.get(
    "/",
    response_model=list[ExpenseResponse],
    dependencies=[Depends(require_authenticated_user)]
)
def get_expenses(
    db: Session = Depends(get_db)
):
    """Get all expenses."""

    return controller.get_all(db)


@router.get(
    "/{expense_id}",
    response_model=ExpenseResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):
    """Get an expense by ID."""

    return controller.get_by_id(
        db,
        expense_id
    )


@router.put(
    "/{expense_id}",
    response_model=ExpenseResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def update_expense(
    expense_id: int,
    data: ExpenseUpdate,
    db: Session = Depends(get_db)
):
    """Update an expense completely."""

    return controller.update(
        db,
        expense_id,
        data
    )


@router.patch(
    "/{expense_id}",
    response_model=ExpenseResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def patch_expense(
    expense_id: int,
    data: ExpensePatch,
    db: Session = Depends(get_db)
):
    """Partially update an expense."""

    return controller.patch(
        db,
        expense_id,
        data
    )


@router.delete(
    "/{expense_id}",
    dependencies=[Depends(require_authenticated_user)]
)
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):
    """Delete an expense."""

    return controller.delete(
        db,
        expense_id
    )