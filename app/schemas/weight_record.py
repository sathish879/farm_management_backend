from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class WeightRecordCreate(BaseModel):
    animal_id: int
    weight_date: date
    weight: Decimal
    unit: str
    notes: str | None = None


class WeightRecordUpdate(BaseModel):
    animal_id: int
    weight_date: date
    weight: Decimal
    unit: str
    notes: str | None = None


class WeightRecordPatch(BaseModel):
    animal_id: int | None = None
    weight_date: date | None = None
    weight: Decimal | None = None
    unit: str | None = None
    notes: str | None = None


class WeightRecordResponse(BaseModel):
    id: int
    animal_id: int
    weight_date: date
    weight: Decimal
    unit: str
    notes: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)