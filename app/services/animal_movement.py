from sqlalchemy.orm import Session

from app.models.animal_movement import AnimalMovement
from app.repositories import animal_movement as movement_repository


def create_movement(db: Session, movement_data) -> AnimalMovement:
    """Create a new animal movement."""

    movement = AnimalMovement(
        animal_id=movement_data.animal_id,
        movement_type=movement_data.movement_type,
        movement_date=movement_data.movement_date,
        reason=movement_data.reason,
        notes=movement_data.notes,
    )

    return movement_repository.create_movement(db, movement)


def get_all_movements(db: Session) -> list[AnimalMovement]:
    """Get all animal movements."""

    return movement_repository.get_all_movements(db)


def get_movement_by_id(
    db: Session,
    movement_id: int
) -> AnimalMovement | None:
    """Get one animal movement by ID."""

    return movement_repository.get_movement_by_id(
        db,
        movement_id
    )


def update_movement(
    db: Session,
    movement_id: int,
    movement_data
) -> AnimalMovement | None:
    """Update an existing animal movement."""

    movement = movement_repository.get_movement_by_id(
        db,
        movement_id
    )

    if movement is None:
        return None

    data = movement_data.model_dump()

    return movement_repository.update_movement(
        db,
        movement,
        data
    )


def patch_movement(
    db: Session,
    movement_id: int,
    movement_data
) -> AnimalMovement | None:
    """Partially update an animal movement."""

    movement = movement_repository.get_movement_by_id(
        db,
        movement_id
    )

    if movement is None:
        return None

    data = movement_data.model_dump(
        exclude_unset=True
    )

    return movement_repository.update_movement(
        db,
        movement,
        data
    )


def delete_movement(
    db: Session,
    movement_id: int
) -> bool:
    """Delete an animal movement."""

    movement = movement_repository.get_movement_by_id(
        db,
        movement_id
    )

    if movement is None:
        return False

    movement_repository.delete_movement(
        db,
        movement
    )

    return True