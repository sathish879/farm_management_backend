from sqlalchemy.orm import Session

from app.models.income import Income
from app.repositories.income import IncomeRepository
from app.schemas.income import (
    IncomeCreate,
    IncomeUpdate,
    IncomePatch,
)


class IncomeService:

    def __init__(self):
        self.repository = IncomeRepository()

    def create(
        self,
        db: Session,
        data: IncomeCreate
    ) -> Income:

        income = Income(
            farm_id=data.farm_id,
            animal_id=data.animal_id,
            income_date=data.income_date,
            category=data.category,
            amount=data.amount,
            description=data.description
        )

        return self.repository.create(
            db,
            income
        )

    def get_all(
        self,
        db: Session
    ) -> list[Income]:

        return self.repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        income_id: int
    ) -> Income | None:

        return self.repository.get_by_id(
            db,
            income_id
        )

    def update(
        self,
        db: Session,
        income_id: int,
        data: IncomeUpdate
    ) -> Income | None:

        income = self.repository.get_by_id(
            db,
            income_id
        )

        if not income:
            return None

        income.farm_id = data.farm_id
        income.animal_id = data.animal_id
        income.income_date = data.income_date
        income.category = data.category
        income.amount = data.amount
        income.description = data.description

        return self.repository.update(
            db,
            income
        )

    def patch(
        self,
        db: Session,
        income_id: int,
        data: IncomePatch
    ) -> Income | None:

        income = self.repository.get_by_id(
            db,
            income_id
        )

        if not income:
            return None

        update_data = data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(
                income,
                field,
                value
            )

        return self.repository.update(
            db,
            income
        )

    def delete(
        self,
        db: Session,
        income_id: int
    ) -> bool:

        income = self.repository.get_by_id(
            db,
            income_id
        )

        if not income:
            return False

        self.repository.delete(
            db,
            income
        )

        return True