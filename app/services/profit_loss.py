from decimal import Decimal

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.income import Income
from app.models.expense import Expense


class ProfitLossService:

    def get_profit_loss(
        self,
        db: Session,
        farm_id: int
    ) -> dict:

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

        net_profit_loss = (
            total_income - total_expense
        )

        if net_profit_loss > 0:
            status = "PROFIT"
        elif net_profit_loss < 0:
            status = "LOSS"
        else:
            status = "BREAK_EVEN"

        return {
            "farm_id": farm_id,
            "total_income": total_income,
            "total_expense": total_expense,
            "net_profit_loss": net_profit_loss,
            "status": status
        }