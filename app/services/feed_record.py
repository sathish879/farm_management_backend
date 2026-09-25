from sqlalchemy.orm import Session

from app.models.feed_record import FeedRecord
from app.repositories.feed_record import FeedRecordRepository
from app.schemas.feed_record import (
    FeedRecordCreate,
    FeedRecordUpdate,
    FeedRecordPatch,
)


class FeedRecordService:

    def __init__(self):
        self.repository = FeedRecordRepository()

    def create(
        self,
        db: Session,
        data: FeedRecordCreate
    ) -> FeedRecord:

        feed_record = FeedRecord(
            animal_id=data.animal_id,
            feed_type_id=data.feed_type_id,
            feed_date=data.feed_date,
            quantity=data.quantity,
            cost=data.cost,
            notes=data.notes
        )

        return self.repository.create(db, feed_record)

    def get_all(
        self,
        db: Session
    ) -> list[FeedRecord]:

        return self.repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        feed_record_id: int
    ) -> FeedRecord | None:

        return self.repository.get_by_id(
            db,
            feed_record_id
        )

    def update(
        self,
        db: Session,
        feed_record_id: int,
        data: FeedRecordUpdate
    ) -> FeedRecord | None:

        feed_record = self.repository.get_by_id(
            db,
            feed_record_id
        )

        if not feed_record:
            return None

        feed_record.animal_id = data.animal_id
        feed_record.feed_type_id = data.feed_type_id
        feed_record.feed_date = data.feed_date
        feed_record.quantity = data.quantity
        feed_record.cost = data.cost
        feed_record.notes = data.notes

        return self.repository.update(
            db,
            feed_record
        )

    def patch(
        self,
        db: Session,
        feed_record_id: int,
        data: FeedRecordPatch
    ) -> FeedRecord | None:

        feed_record = self.repository.get_by_id(
            db,
            feed_record_id
        )

        if not feed_record:
            return None

        update_data = data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(feed_record, field, value)

        return self.repository.update(
            db,
            feed_record
        )

    def delete(
        self,
        db: Session,
        feed_record_id: int
    ) -> bool:

        feed_record = self.repository.get_by_id(
            db,
            feed_record_id
        )

        if not feed_record:
            return False

        self.repository.delete(
            db,
            feed_record
        )

        return True