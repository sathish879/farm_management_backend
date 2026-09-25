from sqlalchemy.orm import Session

from app.models.feed_record import FeedRecord


class FeedRecordRepository:

    def create(
        self,
        db: Session,
        feed_record: FeedRecord
    ) -> FeedRecord:

        db.add(feed_record)
        db.commit()
        db.refresh(feed_record)

        return feed_record

    def get_all(
        self,
        db: Session
    ) -> list[FeedRecord]:

        return db.query(FeedRecord).all()

    def get_by_id(
        self,
        db: Session,
        feed_record_id: int
    ) -> FeedRecord | None:

        return (
            db.query(FeedRecord)
            .filter(FeedRecord.id == feed_record_id)
            .first()
        )

    def update(
        self,
        db: Session,
        feed_record: FeedRecord
    ) -> FeedRecord:

        db.commit()
        db.refresh(feed_record)

        return feed_record

    def delete(
        self,
        db: Session,
        feed_record: FeedRecord
    ) -> None:

        db.delete(feed_record)
        db.commit()