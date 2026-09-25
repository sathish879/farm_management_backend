from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers import feed_type as feed_type_controller
from app.core.dependencies import get_db
from app.core.roles import require_authenticated_user
from app.schemas.feed_type import (
    FeedTypeCreate,
    FeedTypePatch,
    FeedTypeResponse,
    FeedTypeUpdate,
)


router = APIRouter(
    prefix="/feed-types",
    tags=["Feed Types"]
)


@router.post(
    "/",
    response_model=FeedTypeResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def create_feed_type(
    feed_type_data: FeedTypeCreate,
    db: Session = Depends(get_db)
):
    """Create a new feed type."""

    return feed_type_controller.create_feed_type(
        db,
        feed_type_data
    )


@router.get(
    "/",
    response_model=list[FeedTypeResponse],
    dependencies=[Depends(require_authenticated_user)]
)
def get_all_feed_types(
    db: Session = Depends(get_db)
):
    """Get all feed types."""

    return feed_type_controller.get_all_feed_types(db)


@router.get(
    "/{feed_type_id}",
    response_model=FeedTypeResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def get_feed_type_by_id(
    feed_type_id: int,
    db: Session = Depends(get_db)
):
    """Get a feed type by ID."""

    feed_type = feed_type_controller.get_feed_type_by_id(
        db,
        feed_type_id
    )

    if feed_type is None:
        raise HTTPException(
            status_code=404,
            detail="Feed type not found"
        )

    return feed_type


@router.put(
    "/{feed_type_id}",
    response_model=FeedTypeResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def update_feed_type(
    feed_type_id: int,
    feed_type_data: FeedTypeUpdate,
    db: Session = Depends(get_db)
):
    """Update a feed type completely."""

    feed_type = feed_type_controller.update_feed_type(
        db,
        feed_type_id,
        feed_type_data
    )

    if feed_type is None:
        raise HTTPException(
            status_code=404,
            detail="Feed type not found"
        )

    return feed_type


@router.patch(
    "/{feed_type_id}",
    response_model=FeedTypeResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def patch_feed_type(
    feed_type_id: int,
    feed_type_data: FeedTypePatch,
    db: Session = Depends(get_db)
):
    """Partially update a feed type."""

    feed_type = feed_type_controller.patch_feed_type(
        db,
        feed_type_id,
        feed_type_data
    )

    if feed_type is None:
        raise HTTPException(
            status_code=404,
            detail="Feed type not found"
        )

    return feed_type


@router.delete(
    "/{feed_type_id}",
    dependencies=[Depends(require_authenticated_user)]
)
def delete_feed_type(
    feed_type_id: int,
    db: Session = Depends(get_db)
):
    """Delete a feed type."""

    deleted = feed_type_controller.delete_feed_type(
        db,
        feed_type_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Feed type not found"
        )

    return {
        "message": "Feed type deleted successfully"
    }