from sqlalchemy.orm import Session

from app.models.feed_type import FeedType


def create_feed_type(
    db: Session,
    feed_type: FeedType
) -> FeedType:
    """Create a new feed type."""

    db.add(feed_type)
    db.commit()
    db.refresh(feed_type)

    return feed_type


def get_all_feed_types(
    db: Session
) -> list[FeedType]:
    """Return all feed types."""

    return db.query(FeedType).all()


def get_feed_type_by_id(
    db: Session,
    feed_type_id: int
) -> FeedType | None:
    """Return one feed type by ID."""

    return (
        db.query(FeedType)
        .filter(FeedType.id == feed_type_id)
        .first()
    )


def update_feed_type(
    db: Session,
    feed_type: FeedType,
    feed_type_data: dict
) -> FeedType:
    """Update an existing feed type."""

    for field, value in feed_type_data.items():
        setattr(feed_type, field, value)

    db.commit()
    db.refresh(feed_type)

    return feed_type


def delete_feed_type(
    db: Session,
    feed_type: FeedType
) -> None:
    """Delete a feed type."""

    db.delete(feed_type)
    db.commit()