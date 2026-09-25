from sqlalchemy.orm import Session

from app.models.expense import Expense


class ExpenseRepository:

    def create(
        self,
        db: Session,
        expense: Expense
    ) -> Expense:

        db.add(expense)
        db.commit()
        db.refresh(expense)

        return expense

    def get_all(
        self,
        db: Session
    ) -> list[Expense]:

        return db.query(Expense).all()

    def get_by_id(
        self,
        db: Session,
        expense_id: int
    ) -> Expense | None:

        return (
            db.query(Expense)
            .filter(Expense.id == expense_id)
            .first()
        )

    def update(
        self,
        db: Session,
        expense: Expense
    ) -> Expense:

        db.commit()
        db.refresh(expense)

        return expense

    def delete(
        self,
        db: Session,
        expense: Expense
    ) -> None:

        db.delete(expense)
        db.commit()