from sqlalchemy.orm import Session

from app.schemas.animal import (
    AnimalCreate,
    AnimalPatch,
    AnimalUpdate,
)

from app.services import animal as animal_service


def create_animal(
    db: Session,
    animal_data: AnimalCreate
):
    """Create a new animal."""

    return animal_service.create_animal(
        db,
        animal_data
    )


def get_all_animals(
    db: Session
):
    """Get all animals."""

    return animal_service.get_all_animals(db)


def get_animal_by_id(
    db: Session,
    animal_id: int
):
    """Get an animal by ID."""

    return animal_service.get_animal_by_id(
        db,
        animal_id
    )


def update_animal(
    db: Session,
    animal_id: int,
    animal_data: AnimalUpdate
):
    """Update an animal completely."""

    return animal_service.update_animal(
        db,
        animal_id,
        animal_data
    )


def patch_animal(
    db: Session,
    animal_id: int,
    animal_data: AnimalPatch
):
    """Partially update an animal."""

    return animal_service.patch_animal(
        db,
        animal_id,
        animal_data
    )


def delete_animal(
    db: Session,
    animal_id: int
):
    """Delete an animal."""

    return animal_service.delete_animal(
        db,
        animal_id
    )