from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.sale import (
    SaleCreate,
    SaleUpdate,
    SalePatch,
)
from app.services.sale import SaleService


class SaleController:

    def __init__(self):
        self.service = SaleService()

    def create(
        self,
        db: Session,
        data: SaleCreate
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
        sale_id: int
    ):

        sale = self.service.get_by_id(
            db,
            sale_id
        )

        if not sale:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Sale not found"
            )

        return sale

    def update(
        self,
        db: Session,
        sale_id: int,
        data: SaleUpdate
    ):

        sale = self.service.update(
            db,
            sale_id,
            data
        )

        if not sale:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Sale not found"
            )

        return sale

    def patch(
        self,
        db: Session,
        sale_id: int,
        data: SalePatch
    ):

        sale = self.service.patch(
            db,
            sale_id,
            data
        )

        if not sale:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Sale not found"
            )

        return sale

    def delete(
        self,
        db: Session,
        sale_id: int
    ):

        deleted = self.service.delete(
            db,
            sale_id
        )

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Sale not found"
            )

        return {
            "message": "Sale deleted successfully"
        }