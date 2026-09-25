from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.medicine import (
    MedicineCreate,
    MedicineUpdate,
    MedicinePatch,
)
from app.services.medicine import MedicineService


class MedicineController:

    def __init__(self):
        self.service = MedicineService()

    def create(
        self,
        db: Session,
        data: MedicineCreate
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
        medicine_id: int
    ):

        medicine = self.service.get_by_id(
            db,
            medicine_id
        )

        if not medicine:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medicine not found"
            )

        return medicine

    def update(
        self,
        db: Session,
        medicine_id: int,
        data: MedicineUpdate
    ):

        medicine = self.service.update(
            db,
            medicine_id,
            data
        )

        if not medicine:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medicine not found"
            )

        return medicine

    def patch(
        self,
        db: Session,
        medicine_id: int,
        data: MedicinePatch
    ):

        medicine = self.service.patch(
            db,
            medicine_id,
            data
        )

        if not medicine:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medicine not found"
            )

        return medicine

    def delete(
        self,
        db: Session,
        medicine_id: int
    ):

        deleted = self.service.delete(
            db,
            medicine_id
        )

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medicine not found"
            )

        return {
            "message": "Medicine deleted successfully"
        }