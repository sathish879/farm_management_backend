from sqlalchemy.orm import Session

from app.models.medicine_record import MedicineRecord


class MedicineRecordRepository:

    def create(
        self,
        db: Session,
        medicine_record: MedicineRecord
    ) -> MedicineRecord:

        db.add(medicine_record)
        db.commit()
        db.refresh(medicine_record)

        return medicine_record

    def get_all(
        self,
        db: Session
    ) -> list[MedicineRecord]:

        return db.query(MedicineRecord).all()

    def get_by_id(
        self,
        db: Session,
        medicine_record_id: int
    ) -> MedicineRecord | None:

        return (
            db.query(MedicineRecord)
            .filter(
                MedicineRecord.id == medicine_record_id
            )
            .first()
        )

    def update(
        self,
        db: Session,
        medicine_record: MedicineRecord
    ) -> MedicineRecord:

        db.commit()
        db.refresh(medicine_record)

        return medicine_record

    def delete(
        self,
        db: Session,
        medicine_record: MedicineRecord
    ) -> None:

        db.delete(medicine_record)
        db.commit()