from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.feed_record import FeedRecordController
from app.core.dependencies import get_db
from app.core.roles import require_authenticated_user
from app.schemas.feed_record import (
    FeedRecordCreate,
    FeedRecordUpdate,
    FeedRecordPatch,
    FeedRecordResponse,
)


router = APIRouter(
    prefix="/feed-records",
    tags=["Feed Records"]
)

controller = FeedRecordController()


@router.post(
    "/",
    response_model=FeedRecordResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_authenticated_user)]
)
def create_feed_record(
    data: FeedRecordCreate,
    db: Session = Depends(get_db)
):
    """Create a new feed record."""

    return controller.create(
        db,
        data
    )


@router.get(
    "/",
    response_model=list[FeedRecordResponse],
    dependencies=[Depends(require_authenticated_user)]
)
def get_feed_records(
    db: Session = Depends(get_db)
):
    """Get all feed records."""

    return controller.get_all(db)


@router.get(
    "/{feed_record_id}",
    response_model=FeedRecordResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def get_feed_record(
    feed_record_id: int,
    db: Session = Depends(get_db)
):
    """Get a feed record by ID."""

    return controller.get_by_id(
        db,
        feed_record_id
    )


@router.put(
    "/{feed_record_id}",
    response_model=FeedRecordResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def update_feed_record(
    feed_record_id: int,
    data: FeedRecordUpdate,
    db: Session = Depends(get_db)
):
    """Update a feed record completely."""

    return controller.update(
        db,
        feed_record_id,
        data
    )


@router.patch(
    "/{feed_record_id}",
    response_model=FeedRecordResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def patch_feed_record(
    feed_record_id: int,
    data: FeedRecordPatch,
    db: Session = Depends(get_db)
):
    """Partially update a feed record."""

    return controller.patch(
        db,
        feed_record_id,
        data
    )


@router.delete(
    "/{feed_record_id}",
    dependencies=[Depends(require_authenticated_user)]
)
def delete_feed_record(
    feed_record_id: int,
    db: Session = Depends(get_db)
):
    """Delete a feed record."""

    return controller.delete(
        db,
        feed_record_id
    )