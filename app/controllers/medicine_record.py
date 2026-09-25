from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.medicine_record import (
    MedicineRecordCreate,
    MedicineRecordUpdate,
    MedicineRecordPatch,
)
from app.services.medicine_record import MedicineRecordService


class MedicineRecordController:

    def __init__(self):
        self.service = MedicineRecordService()

    def create(
        self,
        db: Session,
        data: MedicineRecordCreate
    ):

        return self.service.create(
            db,
            data
        )

    def get_all(
        self,
        db: Session
    ):

        return self.service.get_all(db)

    def get_by_id(
        self,
        db: Session,
        medicine_record_id: int
    ):

        medicine_record = self.service.get_by_id(
            db,
            medicine_record_id
        )

        if not medicine_record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medicine record not found"
            )

        return medicine_record

    def update(
        self,
        db: Session,
        medicine_record_id: int,
        data: MedicineRecordUpdate
    ):

        medicine_record = self.service.update(
            db,
            medicine_record_id,
            data
        )

        if not medicine_record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medicine record not found"
            )

        return medicine_record

    def patch(
        self,
        db: Session,
        medicine_record_id: int,
        data: MedicineRecordPatch
    ):

        medicine_record = self.service.patch(
            db,
            medicine_record_id,
            data
        )

        if not medicine_record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medicine record not found"
            )

        return medicine_record

    def delete(
        self,
        db: Session,
        medicine_record_id: int
    ):

        deleted = self.service.delete(
            db,
            medicine_record_id
        )

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medicine record not found"
            )

        return {
            "message": "Medicine record deleted successfully"
        }