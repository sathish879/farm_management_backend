from sqlalchemy.orm import Session

from app.models.medicine import Medicine
from app.repositories.medicine import MedicineRepository
from app.schemas.medicine import (
    MedicineCreate,
    MedicineUpdate,
    MedicinePatch,
)


class MedicineService:

    def __init__(self):
        self.repository = MedicineRepository()

    def create(
        self,
        db: Session,
        data: MedicineCreate
    ) -> Medicine:

        medicine = Medicine(
            name=data.name,
            generic_name=data.generic_name,
            medicine_type=data.medicine_type,
            unit=data.unit,
            manufacturer=data.manufacturer,
            description=data.description
        )

        return self.repository.create(
            db,
            medicine
        )

    def get_all(
        self,
        db: Session
    ) -> list[Medicine]:

        return self.repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        medicine_id: int
    ) -> Medicine | None:

        return self.repository.get_by_id(
            db,
            medicine_id
        )

    def update(
        self,
        db: Session,
        medicine_id: int,
        data: MedicineUpdate
    ) -> Medicine | None:

        medicine = self.repository.get_by_id(
            db,
            medicine_id
        )

        if not medicine:
            return None

        medicine.name = data.name
        medicine.generic_name = data.generic_name
        medicine.medicine_type = data.medicine_type
        medicine.unit = data.unit
        medicine.manufacturer = data.manufacturer
        medicine.description = data.description

        return self.repository.update(
            db,
            medicine
        )

    def patch(
        self,
        db: Session,
        medicine_id: int,
        data: MedicinePatch
    ) -> Medicine | None:

        medicine = self.repository.get_by_id(
            db,
            medicine_id
        )

        if not medicine:
            return None

        update_data = data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(medicine, field, value)

        return self.repository.update(
            db,
            medicine
        )

    def delete(
        self,
        db: Session,
        medicine_id: int
    ) -> bool:

        medicine = self.repository.get_by_id(
            db,
            medicine_id
        )

        if not medicine:
            return False

        self.repository.delete(
            db,
            medicine
        )

        return True