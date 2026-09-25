from sqlalchemy.orm import Session

from app.models.expense import Expense
from app.repositories.expense import ExpenseRepository
from app.schemas.expense import (
    ExpenseCreate,
    ExpenseUpdate,
    ExpensePatch,
)


class ExpenseService:

    def __init__(self):
        self.repository = ExpenseRepository()

    def create(
        self,
        db: Session,
        data: ExpenseCreate
    ) -> Expense:

        expense = Expense(
            farm_id=data.farm_id,
            animal_id=data.animal_id,
            expense_date=data.expense_date,
            category=data.category,
            amount=data.amount,
            description=data.description
        )

        return self.repository.create(
            db,
            expense
        )

    def get_all(
        self,
        db: Session
    ) -> list[Expense]:

        return self.repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        expense_id: int
    ) -> Expense | None:

        return self.repository.get_by_id(
            db,
            expense_id
        )

    def update(
        self,
        db: Session,
        expense_id: int,
        data: ExpenseUpdate
    ) -> Expense | None:

        expense = self.repository.get_by_id(
            db,
            expense_id
        )

        if not expense:
            return None

        expense.farm_id = data.farm_id
        expense.animal_id = data.animal_id
        expense.expense_date = data.expense_date
        expense.category = data.category
        expense.amount = data.amount
        expense.description = data.description

        return self.repository.update(
            db,
            expense
        )

    def patch(
        self,
        db: Session,
        expense_id: int,
        data: ExpensePatch
    ) -> Expense | None:

        expense = self.repository.get_by_id(
            db,
            expense_id
        )

        if not expense:
            return None

        update_data = data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(
                expense,
                field,
                value
            )

        return self.repository.update(
            db,
            expense
        )

    def delete(
        self,
        db: Session,
        expense_id: int
    ) -> bool:

        expense = self.repository.get_by_id(
            db,
            expense_id
        )

        if not expense:
            return False

        self.repository.delete(
            db,
            expense
        )

        return True