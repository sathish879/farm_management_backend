from decimal import Decimal

from pydantic import BaseModel


class DashboardResponse(BaseModel):
    farm_id: int

    total_animals: int
    active_animals: int
    sold_animals: int

    total_feed_cost: Decimal
    total_medicine_cost: Decimal

    total_income: Decimal
    total_expense: Decimal

    profit_loss: Decimal