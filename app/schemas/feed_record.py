from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class FeedRecordCreate(BaseModel):
    animal_id: int
    feed_type_id: int
    feed_date: date
    quantity: Decimal
    cost: Decimal
    notes: str | None = None


class FeedRecordUpdate(BaseModel):
    animal_id: int
    feed_type_id: int
    feed_date: date
    quantity: Decimal
    cost: Decimal
    notes: str | None = None


class FeedRecordPatch(BaseModel):
    animal_id: int | None = None
    feed_type_id: int | None = None
    feed_date: date | None = None
    quantity: Decimal | None = None
    cost: Decimal | None = None
    notes: str | None = None


class FeedRecordResponse(BaseModel):
    id: int
    animal_id: int
    feed_type_id: int
    feed_date: date
    quantity: Decimal
    cost: Decimal
    notes: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)