from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.feed_record import (
    FeedRecordCreate,
    FeedRecordUpdate,
    FeedRecordPatch,
)
from app.services.feed_record import FeedRecordService


class FeedRecordController:

    def __init__(self):
        self.service = FeedRecordService()

    def create(
        self,
        db: Session,
        data: FeedRecordCreate
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
        feed_record_id: int
    ):

        feed_record = self.service.get_by_id(
            db,
            feed_record_id
        )

        if not feed_record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Feed record not found"
            )

        return feed_record

    def update(
        self,
        db: Session,
        feed_record_id: int,
        data: FeedRecordUpdate
    ):

        feed_record = self.service.update(
            db,
            feed_record_id,
            data
        )

        if not feed_record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Feed record not found"
            )

        return feed_record

    def patch(
        self,
        db: Session,
        feed_record_id: int,
        data: FeedRecordPatch
    ):

        feed_record = self.service.patch(
            db,
            feed_record_id,
            data
        )

        if not feed_record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Feed record not found"
            )

        return feed_record

    def delete(
        self,
        db: Session,
        feed_record_id: int
    ):

        deleted = self.service.delete(
            db,
            feed_record_id
        )

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Feed record not found"
            )

        return {
            "message": "Feed record deleted successfully"
        }