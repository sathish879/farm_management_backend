from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.weight_record import (
    WeightRecordCreate,
    WeightRecordUpdate,
    WeightRecordPatch,
)
from app.services.weight_record import WeightRecordService


class WeightRecordController:

    def __init__(self):
        self.service = WeightRecordService()

    def create(
        self,
        db: Session,
        data: WeightRecordCreate
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
        weight_record_id: int
    ):

        weight_record = self.service.get_by_id(
            db,
            weight_record_id
        )

        if not weight_record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Weight record not found"
            )

        return weight_record

    def update(
        self,
        db: Session,
        weight_record_id: int,
        data: WeightRecordUpdate
    ):

        weight_record = self.service.update(
            db,
            weight_record_id,
            data
        )

        if not weight_record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Weight record not found"
            )

        return weight_record

    def patch(
        self,
        db: Session,
        weight_record_id: int,
        data: WeightRecordPatch
    ):

        weight_record = self.service.patch(
            db,
            weight_record_id,
            data
        )

        if not weight_record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Weight record not found"
            )

        return weight_record

    def delete(
        self,
        db: Session,
        weight_record_id: int
    ):

        deleted = self.service.delete(
            db,
            weight_record_id
        )

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Weight record not found"
            )

        return {
            "message": "Weight record deleted successfully"
        }