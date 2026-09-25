from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class SaleCreate(BaseModel):
    animal_id: int
    sale_date: date
    buyer_name: str
    buyer_phone: str | None = None
    sale_price: Decimal
    sale_status: str = "COMPLETED"
    notes: str | None = None


class SaleUpdate(BaseModel):
    animal_id: int
    sale_date: date
    buyer_name: str
    buyer_phone: str | None = None
    sale_price: Decimal
    sale_status: str
    notes: str | None = None


class SalePatch(BaseModel):
    animal_id: int | None = None
    sale_date: date | None = None
    buyer_name: str | None = None
    buyer_phone: str | None = None
    sale_price: Decimal | None = None
    sale_status: str | None = None
    notes: str | None = None


class SaleResponse(BaseModel):
    id: int
    animal_id: int
    sale_date: date
    buyer_name: str
    buyer_phone: str | None
    sale_price: Decimal
    sale_status: str
    notes: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)