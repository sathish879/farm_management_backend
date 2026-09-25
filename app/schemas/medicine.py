from datetime import datetime

from pydantic import BaseModel, ConfigDict


class MedicineCreate(BaseModel):
    name: str
    generic_name: str | None = None
    medicine_type: str
    unit: str
    manufacturer: str | None = None
    description: str | None = None


class MedicineUpdate(BaseModel):
    name: str
    generic_name: str | None = None
    medicine_type: str
    unit: str
    manufacturer: str | None = None
    description: str | None = None


class MedicinePatch(BaseModel):
    name: str | None = None
    generic_name: str | None = None
    medicine_type: str | None = None
    unit: str | None = None
    manufacturer: str | None = None
    description: str | None = None


class MedicineResponse(BaseModel):
    id: int
    name: str
    generic_name: str | None
    medicine_type: str
    unit: str
    manufacturer: str | None
    description: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)