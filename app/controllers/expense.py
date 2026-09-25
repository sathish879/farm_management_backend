from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.expense import (
    ExpenseCreate,
    ExpenseUpdate,
    ExpensePatch,
)
from app.services.expense import ExpenseService


class ExpenseController:

    def __init__(self):
        self.service = ExpenseService()

    def create(
        self,
        db: Session,
        data: ExpenseCreate
    ):

        return self.service.create(
            db,
            data
        )

    def get_all(
        self,
        db: Session
    ):

        return self.service.get_all(db)

    def get_by_id(
        self,
        db: Session,
        expense_id: int
    ):

        expense = self.service.get_by_id(
            db,
            expense_id
        )

        if not expense:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Expense not found"
            )

        return expense

    def update(
        self,
        db: Session,
        expense_id: int,
        data: ExpenseUpdate
    ):

        expense = self.service.update(
            db,
            expense_id,
            data
        )

        if not expense:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Expense not found"
            )

        return expense

    def patch(
        self,
        db: Session,
        expense_id: int,
        data: ExpensePatch
    ):

        expense = self.service.patch(
            db,
            expense_id,
            data
        )

        if not expense:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Expense not found"
            )

        return expense

    def delete(
        self,
        db: Session,
        expense_id: int
    ):

        deleted = self.service.delete(
            db,
            expense_id
        )

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Expense not found"
            )

        return {
            "message": "Expense deleted successfully"
        }