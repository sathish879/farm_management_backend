from sqlalchemy.orm import Session

from app.models.weight_record import WeightRecord


class WeightRecordRepository:

    def create(
        self,
        db: Session,
        weight_record: WeightRecord
    ) -> WeightRecord:

        db.add(weight_record)
        db.commit()
        db.refresh(weight_record)

        return weight_record

    def get_all(
        self,
        db: Session
    ) -> list[WeightRecord]:

        return db.query(WeightRecord).all()

    def get_by_id(
        self,
        db: Session,
        weight_record_id: int
    ) -> WeightRecord | None:

        return (
            db.query(WeightRecord)
            .filter(
                WeightRecord.id == weight_record_id
            )
            .first()
        )

    def update(
        self,
        db: Session,
        weight_record: WeightRecord
    ) -> WeightRecord:

        db.commit()
        db.refresh(weight_record)

        return weight_record

    def delete(
        self,
        db: Session,
        weight_record: WeightRecord
    ) -> None:

        db.delete(weight_record)
        db.commit()