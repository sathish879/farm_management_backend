from sqlalchemy.orm import Session

from app.models.income import Income


class IncomeRepository:

    def create(
        self,
        db: Session,
        income: Income
    ) -> Income:

        db.add(income)
        db.commit()
        db.refresh(income)

        return income

    def get_all(
        self,
        db: Session
    ) -> list[Income]:

        return db.query(Income).all()

    def get_by_id(
        self,
        db: Session,
        income_id: int
    ) -> Income | None:

        return (
            db.query(Income)
            .filter(Income.id == income_id)
            .first()
        )

    def update(
        self,
        db: Session,
        income: Income
    ) -> Income:

        db.commit()
        db.refresh(income)

        return income

    def delete(
        self,
        db: Session,
        income: Income
    ) -> None:

        db.delete(income)
        db.commit()