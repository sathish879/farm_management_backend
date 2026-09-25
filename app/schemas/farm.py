from datetime import datetime

from pydantic import BaseModel, ConfigDict


class FarmCreate(BaseModel):
    farm_code: str
    name: str
    location: str
    owner_name: str
    phone: str


class FarmUpdate(BaseModel):
    farm_code: str
    name: str
    location: str
    owner_name: str
    phone: str


class FarmPatch(BaseModel):
    farm_code: str | None = None
    name: str | None = None
    location: str | None = None
    owner_name: str | None = None
    phone: str | None = None


class FarmResponse(BaseModel):
    id: int
    farm_code: str
    name: str
    location: str
    owner_name: str
    phone: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)