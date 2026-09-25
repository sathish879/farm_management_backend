from sqlalchemy.orm import Session

from app.models.sale import Sale
from app.repositories.sale import SaleRepository
from app.schemas.sale import (
    SaleCreate,
    SaleUpdate,
    SalePatch,
)


class SaleService:

    def __init__(self):
        self.repository = SaleRepository()

    def create(
        self,
        db: Session,
        data: SaleCreate
    ) -> Sale:

        sale = Sale(
            animal_id=data.animal_id,
            sale_date=data.sale_date,
            buyer_name=data.buyer_name,
            buyer_phone=data.buyer_phone,
            sale_price=data.sale_price,
            sale_status=data.sale_status,
            notes=data.notes
        )

        return self.repository.create(
            db,
            sale
        )

    def get_all(
        self,
        db: Session
    ) -> list[Sale]:

        return self.repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        sale_id: int
    ) -> Sale | None:

        return self.repository.get_by_id(
            db,
            sale_id
        )

    def update(
        self,
        db: Session,
        sale_id: int,
        data: SaleUpdate
    ) -> Sale | None:

        sale = self.repository.get_by_id(
            db,
            sale_id
        )

        if not sale:
            return None

        sale.animal_id = data.animal_id
        sale.sale_date = data.sale_date
        sale.buyer_name = data.buyer_name
        sale.buyer_phone = data.buyer_phone
        sale.sale_price = data.sale_price
        sale.sale_status = data.sale_status
        sale.notes = data.notes

        return self.repository.update(
            db,
            sale
        )

    def patch(
        self,
        db: Session,
        sale_id: int,
        data: SalePatch
    ) -> Sale | None:

        sale = self.repository.get_by_id(
            db,
            sale_id
        )

        if not sale:
            return None

        update_data = data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(
                sale,
                field,
                value
            )

        return self.repository.update(
            db,
            sale
        )

    def delete(
        self,
        db: Session,
        sale_id: int
    ) -> bool:

        sale = self.repository.get_by_id(
            db,
            sale_id
        )

        if not sale:
            return False

        self.repository.delete(
            db,
            sale
        )

        return True