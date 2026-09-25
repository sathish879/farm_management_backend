from sqlalchemy.orm import Session

from app.models.feed_type import FeedType
from app.repositories import feed_type as feed_type_repository


def create_feed_type(
    db: Session,
    feed_type_data
) -> FeedType:
    """Create a new feed type."""

    feed_type = FeedType(
        name=feed_type_data.name,
        description=feed_type_data.description,
        unit=feed_type_data.unit,
    )

    return feed_type_repository.create_feed_type(
        db,
        feed_type
    )


def get_all_feed_types(
    db: Session
) -> list[FeedType]:
    """Get all feed types."""

    return feed_type_repository.get_all_feed_types(db)


def get_feed_type_by_id(
    db: Session,
    feed_type_id: int
) -> FeedType | None:
    """Get a feed type by ID."""

    return feed_type_repository.get_feed_type_by_id(
        db,
        feed_type_id
    )


def update_feed_type(
    db: Session,
    feed_type_id: int,
    feed_type_data
) -> FeedType | None:
    """Update a feed type completely."""

    feed_type = feed_type_repository.get_feed_type_by_id(
        db,
        feed_type_id
    )

    if feed_type is None:
        return None

    data = feed_type_data.model_dump()

    return feed_type_repository.update_feed_type(
        db,
        feed_type,
        data
    )


def patch_feed_type(
    db: Session,
    feed_type_id: int,
    feed_type_data
) -> FeedType | None:
    """Partially update a feed type."""

    feed_type = feed_type_repository.get_feed_type_by_id(
        db,
        feed_type_id
    )

    if feed_type is None:
        return None

    data = feed_type_data.model_dump(
        exclude_unset=True
    )

    return feed_type_repository.update_feed_type(
        db,
        feed_type,
        data
    )


def delete_feed_type(
    db: Session,
    feed_type_id: int
) -> bool:
    """Delete a feed type."""

    feed_type = feed_type_repository.get_feed_type_by_id(
        db,
        feed_type_id
    )

    if feed_type is None:
        return False

    feed_type_repository.delete_feed_type(
        db,
        feed_type
    )

    return True