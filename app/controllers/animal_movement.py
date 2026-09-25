from sqlalchemy.orm import Session

from app.schemas.animal_movement import (
    AnimalMovementCreate,
    AnimalMovementPatch,
    AnimalMovementUpdate,
)
from app.services import animal_movement as movement_service


def create_movement(
    db: Session,
    movement_data: AnimalMovementCreate
):
    """Create a new animal movement."""

    return movement_service.create_movement(
        db,
        movement_data
    )


def get_all_movements(db: Session):
    """Get all animal movements."""

    return movement_service.get_all_movements(db)


def get_movement_by_id(
    db: Session,
    movement_id: int
):
    """Get an animal movement by ID."""

    return movement_service.get_movement_by_id(
        db,
        movement_id
    )


def update_movement(
    db: Session,
    movement_id: int,
    movement_data: AnimalMovementUpdate
):
    """Update an animal movement completely."""

    return movement_service.update_movement(
        db,
        movement_id,
        movement_data
    )


def patch_movement(
    db: Session,
    movement_id: int,
    movement_data: AnimalMovementPatch
):
    """Partially update an animal movement."""

    return movement_service.patch_movement(
        db,
        movement_id,
        movement_data
    )


def delete_movement(
    db: Session,
    movement_id: int
):
    """Delete an animal movement."""

    return movement_service.delete_movement(
        db,
        movement_id
    )