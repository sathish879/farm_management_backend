from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class MedicineRecordCreate(BaseModel):
    animal_id: int
    medicine_id: int
    treatment_date: date
    dosage: str
    reason: str
    cost: Decimal
    veterinarian: str | None = None
    withdrawal_days: int | None = None
    notes: str | None = None


class MedicineRecordUpdate(BaseModel):
    animal_id: int
    medicine_id: int
    treatment_date: date
    dosage: str
    reason: str
    cost: Decimal
    veterinarian: str | None = None
    withdrawal_days: int | None = None
    notes: str | None = None


class MedicineRecordPatch(BaseModel):
    animal_id: int | None = None
    medicine_id: int | None = None
    treatment_date: date | None = None
    dosage: str | None = None
    reason: str | None = None
    cost: Decimal | None = None
    veterinarian: str | None = None
    withdrawal_days: int | None = None
    notes: str | None = None


class MedicineRecordResponse(BaseModel):
    id: int
    animal_id: int
    medicine_id: int
    treatment_date: date
    dosage: str
    reason: str
    cost: Decimal
    veterinarian: str | None
    withdrawal_days: int | None
    notes: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)