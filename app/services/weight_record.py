from sqlalchemy.orm import Session

from app.models.weight_record import WeightRecord
from app.repositories.weight_record import WeightRecordRepository
from app.schemas.weight_record import (
    WeightRecordCreate,
    WeightRecordUpdate,
    WeightRecordPatch,
)


class WeightRecordService:

    def __init__(self):
        self.repository = WeightRecordRepository()

    def create(
        self,
        db: Session,
        data: WeightRecordCreate
    ) -> WeightRecord:

        weight_record = WeightRecord(
            animal_id=data.animal_id,
            weight_date=data.weight_date,
            weight=data.weight,
            unit=data.unit,
            notes=data.notes
        )

        return self.repository.create(
            db,
            weight_record
        )

    def get_all(
        self,
        db: Session
    ) -> list[WeightRecord]:

        return self.repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        weight_record_id: int
    ) -> WeightRecord | None:

        return self.repository.get_by_id(
            db,
            weight_record_id
        )

    def update(
        self,
        db: Session,
        weight_record_id: int,
        data: WeightRecordUpdate
    ) -> WeightRecord | None:

        weight_record = self.repository.get_by_id(
            db,
            weight_record_id
        )

        if not weight_record:
            return None

        weight_record.animal_id = data.animal_id
        weight_record.weight_date = data.weight_date
        weight_record.weight = data.weight
        weight_record.unit = data.unit
        weight_record.notes = data.notes

        return self.repository.update(
            db,
            weight_record
        )

    def patch(
        self,
        db: Session,
        weight_record_id: int,
        data: WeightRecordPatch
    ) -> WeightRecord | None:

        weight_record = self.repository.get_by_id(
            db,
            weight_record_id
        )

        if not weight_record:
            return None

        update_data = data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(
                weight_record,
                field,
                value
            )

        return self.repository.update(
            db,
            weight_record
        )

    def delete(
        self,
        db: Session,
        weight_record_id: int
    ) -> bool:

        weight_record = self.repository.get_by_id(
            db,
            weight_record_id
        )

        if not weight_record:
            return False

        self.repository.delete(
            db,
            weight_record
        )

        return True