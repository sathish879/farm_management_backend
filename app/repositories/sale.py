from sqlalchemy.orm import Session

from app.models.sale import Sale


class SaleRepository:

    def create(
        self,
        db: Session,
        sale: Sale
    ) -> Sale:

        db.add(sale)
        db.commit()
        db.refresh(sale)

        return sale

    def get_all(
        self,
        db: Session
    ) -> list[Sale]:

        return db.query(Sale).all()

    def get_by_id(
        self,
        db: Session,
        sale_id: int
    ) -> Sale | None:

        return (
            db.query(Sale)
            .filter(Sale.id == sale_id)
            .first()
        )

    def update(
        self,
        db: Session,
        sale: Sale
    ) -> Sale:

        db.commit()
        db.refresh(sale)

        return sale

    def delete(
        self,
        db: Session,
        sale: Sale
    ) -> None:

        db.delete(sale)
        db.commit()