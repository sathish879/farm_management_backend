from sqlalchemy.orm import Session

from app.models.medicine_record import MedicineRecord
from app.repositories.medicine_record import MedicineRecordRepository
from app.schemas.medicine_record import (
    MedicineRecordCreate,
    MedicineRecordUpdate,
    MedicineRecordPatch,
)


class MedicineRecordService:

    def __init__(self):
        self.repository = MedicineRecordRepository()

    def create(
        self,
        db: Session,
        data: MedicineRecordCreate
    ) -> MedicineRecord:

        medicine_record = MedicineRecord(
            animal_id=data.animal_id,
            medicine_id=data.medicine_id,
            treatment_date=data.treatment_date,
            dosage=data.dosage,
            reason=data.reason,
            cost=data.cost,
            veterinarian=data.veterinarian,
            withdrawal_days=data.withdrawal_days,
            notes=data.notes
        )

        return self.repository.create(
            db,
            medicine_record
        )

    def get_all(
        self,
        db: Session
    ) -> list[MedicineRecord]:

        return self.repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        medicine_record_id: int
    ) -> MedicineRecord | None:

        return self.repository.get_by_id(
            db,
            medicine_record_id
        )

    def update(
        self,
        db: Session,
        medicine_record_id: int,
        data: MedicineRecordUpdate
    ) -> MedicineRecord | None:

        medicine_record = self.repository.get_by_id(
            db,
            medicine_record_id
        )

        if not medicine_record:
            return None

        medicine_record.animal_id = data.animal_id
        medicine_record.medicine_id = data.medicine_id
        medicine_record.treatment_date = data.treatment_date
        medicine_record.dosage = data.dosage
        medicine_record.reason = data.reason
        medicine_record.cost = data.cost
        medicine_record.veterinarian = data.veterinarian
        medicine_record.withdrawal_days = data.withdrawal_days
        medicine_record.notes = data.notes

        return self.repository.update(
            db,
            medicine_record
        )

    def patch(
        self,
        db: Session,
        medicine_record_id: int,
        data: MedicineRecordPatch
    ) -> MedicineRecord | None:

        medicine_record = self.repository.get_by_id(
            db,
            medicine_record_id
        )

        if not medicine_record:
            return None

        update_data = data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(
                medicine_record,
                field,
                value
            )

        return self.repository.update(
            db,
            medicine_record
        )

    def delete(
        self,
        db: Session,
        medicine_record_id: int
    ) -> bool:

        medicine_record = self.repository.get_by_id(
            db,
            medicine_record_id
        )

        if not medicine_record:
            return False

        self.repository.delete(
            db,
            medicine_record
        )

        return True