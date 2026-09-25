from datetime import datetime

from pydantic import BaseModel, ConfigDict


class FeedTypeCreate(BaseModel):
    name: str
    description: str | None = None
    unit: str


class FeedTypeUpdate(BaseModel):
    name: str
    description: str | None = None
    unit: str


class FeedTypePatch(BaseModel):
    name: str | None = None
    description: str | None = None
    unit: str | None = None


class FeedTypeResponse(BaseModel):
    id: int
    name: str
    description: str | None
    unit: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)