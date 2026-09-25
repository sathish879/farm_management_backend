from sqlalchemy.orm import Session

from app.models.medicine import Medicine


class MedicineRepository:

    def create(
        self,
        db: Session,
        medicine: Medicine
    ) -> Medicine:

        db.add(medicine)
        db.commit()
        db.refresh(medicine)

        return medicine

    def get_all(
        self,
        db: Session
    ) -> list[Medicine]:

        return db.query(Medicine).all()

    def get_by_id(
        self,
        db: Session,
        medicine_id: int
    ) -> Medicine | None:

        return (
            db.query(Medicine)
            .filter(Medicine.id == medicine_id)
            .first()
        )

    def update(
        self,
        db: Session,
        medicine: Medicine
    ) -> Medicine:

        db.commit()
        db.refresh(medicine)

        return medicine

    def delete(
        self,
        db: Session,
        medicine: Medicine
    ) -> None:

        db.delete(medicine)
        db.commit()