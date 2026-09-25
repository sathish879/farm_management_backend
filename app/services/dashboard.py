from decimal import Decimal

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.animal import Animal
from app.models.feed_record import FeedRecord
from app.models.medicine_record import MedicineRecord
from app.models.income import Income
from app.models.expense import Expense


class DashboardService:

    def get_dashboard(
        self,
        db: Session,
        farm_id: int
    ) -> dict:

        # Count all animals belonging to this farm.
        total_animals = (
            db.query(func.count(Animal.id))
            .filter(Animal.farm_id == farm_id)
            .scalar()
        )

        # Count currently active animals.
        active_animals = (
            db.query(func.count(Animal.id))
            .filter(
                Animal.farm_id == farm_id,
                Animal.status == "ACTIVE"
            )
            .scalar()
        )

        # Count sold animals.
        sold_animals = (
            db.query(func.count(Animal.id))
            .filter(
                Animal.farm_id == farm_id,
                Animal.status == "SOLD"
            )
            .scalar()
        )

        # Calculate total feed cost.
        total_feed_cost = (
            db.query(
                func.coalesce(
                    func.sum(FeedRecord.cost),
                    0
                )
            )
            .join(
                Animal,
                Animal.id == FeedRecord.animal_id
            )
            .filter(
                Animal.farm_id == farm_id
            )
            .scalar()
        )

        # Calculate total medicine cost.
        total_medicine_cost = (
            db.query(
                func.coalesce(
                    func.sum(MedicineRecord.cost),
                    0
                )
            )
            .join(
                Animal,
                Animal.id == MedicineRecord.animal_id
            )
            .filter(
                Animal.farm_id == farm_id
            )
            .scalar()
        )

        # Calculate total income.
        total_income = (
            db.query(
                func.coalesce(
                    func.sum(Income.amount),
                    0
                )
            )
            .filter(
                Income.farm_id == farm_id
            )
            .scalar()
        )

        # Calculate total expenses.
        total_expense = (
            db.query(
                func.coalesce(
                    func.sum(Expense.amount),
                    0
                )
            )
            .filter(
                Expense.farm_id == farm_id
            )
            .scalar()
        )

        total_income = Decimal(total_income)
        total_expense = Decimal(total_expense)

        profit_loss = (
            total_income - total_expense
        )

        return {
            "farm_id": farm_id,
            "total_animals": total_animals or 0,
            "active_animals": active_animals or 0,
            "sold_animals": sold_animals or 0,
            "total_feed_cost": Decimal(total_feed_cost),
            "total_medicine_cost": Decimal(total_medicine_cost),
            "total_income": total_income,
            "total_expense": total_expense,
            "profit_loss": profit_loss
        }