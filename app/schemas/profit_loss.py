from decimal import Decimal

from pydantic import BaseModel


class ProfitLossResponse(BaseModel):
    farm_id: int
    total_income: Decimal
    total_expense: Decimal
    net_profit_loss: Decimal
    status: str