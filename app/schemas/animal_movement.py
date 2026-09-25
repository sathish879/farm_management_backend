from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AnimalMovementCreate(BaseModel):
    animal_id: int
    movement_type: str
    movement_date: datetime
    reason: str
    notes: str | None = None


class AnimalMovementUpdate(BaseModel):
    animal_id: int
    movement_type: str
    movement_date: datetime
    reason: str
    notes: str | None = None


class AnimalMovementPatch(BaseModel):
    animal_id: int | None = None
    movement_type: str | None = None
    movement_date: datetime | None = None
    reason: str | None = None
    notes: str | None = None


class AnimalMovementResponse(BaseModel):
    id: int
    animal_id: int
    movement_type: str
    movement_date: datetime
    reason: str
    notes: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)