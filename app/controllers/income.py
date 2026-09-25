from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.income import (
    IncomeCreate,
    IncomeUpdate,
    IncomePatch,
)
from app.services.income import IncomeService


class IncomeController:

    def __init__(self):
        self.service = IncomeService()

    def create(
        self,
        db: Session,
        data: IncomeCreate
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
        income_id: int
    ):

        income = self.service.get_by_id(
            db,
            income_id
        )

        if not income:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Income not found"
            )

        return income

    def update(
        self,
        db: Session,
        income_id: int,
        data: IncomeUpdate
    ):

        income = self.service.update(
            db,
            income_id,
            data
        )

        if not income:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Income not found"
            )

        return income

    def patch(
        self,
        db: Session,
        income_id: int,
        data: IncomePatch
    ):

        income = self.service.patch(
            db,
            income_id,
            data
        )

        if not income:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Income not found"
            )

        return income

    def delete(
        self,
        db: Session,
        income_id: int
    ):

        deleted = self.service.delete(
            db,
            income_id
        )

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Income not found"
            )

        return {
            "message": "Income deleted successfully"
        }