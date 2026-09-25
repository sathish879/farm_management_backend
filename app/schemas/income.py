from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class IncomeCreate(BaseModel):
    farm_id: int
    animal_id: int | None = None
    income_date: date
    category: str
    amount: Decimal
    description: str | None = None


class IncomeUpdate(BaseModel):
    farm_id: int
    animal_id: int | None = None
    income_date: date
    category: str
    amount: Decimal
    description: str | None = None


class IncomePatch(BaseModel):
    farm_id: int | None = None
    animal_id: int | None = None
    income_date: date | None = None
    category: str | None = None
    amount: Decimal | None = None
    description: str | None = None


class IncomeResponse(BaseModel):
    id: int
    farm_id: int
    animal_id: int | None
    income_date: date
    category: str
    amount: Decimal
    description: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)