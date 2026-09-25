from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ExpenseCreate(BaseModel):
    farm_id: int
    animal_id: int | None = None
    expense_date: date
    category: str
    amount: Decimal
    description: str | None = None


class ExpenseUpdate(BaseModel):
    farm_id: int
    animal_id: int | None = None
    expense_date: date
    category: str
    amount: Decimal
    description: str | None = None


class ExpensePatch(BaseModel):
    farm_id: int | None = None
    animal_id: int | None = None
    expense_date: date | None = None
    category: str | None = None
    amount: Decimal | None = None
    description: str | None = None


class ExpenseResponse(BaseModel):
    id: int
    farm_id: int
    animal_id: int | None
    expense_date: date
    category: str
    amount: Decimal
    description: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)