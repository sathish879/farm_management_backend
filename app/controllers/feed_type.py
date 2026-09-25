from sqlalchemy.orm import Session

from app.schemas.feed_type import (
    FeedTypeCreate,
    FeedTypePatch,
    FeedTypeUpdate,
)

from app.services import feed_type as feed_type_service


def create_feed_type(
    db: Session,
    feed_type_data: FeedTypeCreate
):
    """Create a new feed type."""

    return feed_type_service.create_feed_type(
        db,
        feed_type_data
    )


def get_all_feed_types(
    db: Session
):
    """Get all feed types."""

    return feed_type_service.get_all_feed_types(db)


def get_feed_type_by_id(
    db: Session,
    feed_type_id: int
):
    """Get a feed type by ID."""

    return feed_type_service.get_feed_type_by_id(
        db,
        feed_type_id
    )


def update_feed_type(
    db: Session,
    feed_type_id: int,
    feed_type_data: FeedTypeUpdate
):
    """Update a feed type completely."""

    return feed_type_service.update_feed_type(
        db,
        feed_type_id,
        feed_type_data
    )


def patch_feed_type(
    db: Session,
    feed_type_id: int,
    feed_type_data: FeedTypePatch
):
    """Partially update a feed type."""

    return feed_type_service.patch_feed_type(
        db,
        feed_type_id,
        feed_type_data
    )


def delete_feed_type(
    db: Session,
    feed_type_id: int
):
    """Delete a feed type."""

    return feed_type_service.delete_feed_type(
        db,
        feed_type_id
    )