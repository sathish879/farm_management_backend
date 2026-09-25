from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.services.profit_loss import ProfitLossService


class ProfitLossController:

    def __init__(self):
        self.service = ProfitLossService()

    def get_profit_loss(
        self,
        db: Session,
        farm_id: int
    ):

        result = self.service.get_profit_loss(
            db,
            farm_id
        )

        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Profit/Loss data not found"
            )

        return result