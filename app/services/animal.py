from sqlalchemy.orm import Session

from app.models.animal import Animal
from app.repositories import animal as animal_repository


def create_animal(
    db: Session,
    animal_data
) -> Animal:
    """Create a new animal."""

    animal = Animal(
        animal_code=animal_data.animal_code,
        farm_id=animal_data.farm_id,
        animal_type=animal_data.animal_type,
        breed=animal_data.breed,
        gender=animal_data.gender,
        date_of_birth=animal_data.date_of_birth,
        purchase_date=animal_data.purchase_date,
        purchase_price=animal_data.purchase_price,
        status=animal_data.status,
    )

    return animal_repository.create_animal(
        db,
        animal
    )


def get_all_animals(
    db: Session
) -> list[Animal]:
    """Get all animals."""

    return animal_repository.get_all_animals(db)


def get_animal_by_id(
    db: Session,
    animal_id: int
) -> Animal | None:
    """Get one animal by ID."""

    return animal_repository.get_animal_by_id(
        db,
        animal_id
    )


def update_animal(
    db: Session,
    animal_id: int,
    animal_data
) -> Animal | None:
    """Update an animal completely."""

    animal = animal_repository.get_animal_by_id(
        db,
        animal_id
    )

    if animal is None:
        return None

    data = animal_data.model_dump()

    return animal_repository.update_animal(
        db,
        animal,
        data
    )


def patch_animal(
    db: Session,
    animal_id: int,
    animal_data
) -> Animal | None:
    """Partially update an animal."""

    animal = animal_repository.get_animal_by_id(
        db,
        animal_id
    )

    if animal is None:
        return None

    data = animal_data.model_dump(
        exclude_unset=True
    )

    return animal_repository.update_animal(
        db,
        animal,
        data
    )


def delete_animal(
    db: Session,
    animal_id: int
) -> bool:
    """Delete an animal."""

    animal = animal_repository.get_animal_by_id(
        db,
        animal_id
    )

    if animal is None:
        return False

    animal_repository.delete_animal(
        db,
        animal
    )

    return True