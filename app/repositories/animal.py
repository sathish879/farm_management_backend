from sqlalchemy.orm import Session

from app.models.animal import Animal


def create_animal(
    db: Session,
    animal: Animal
) -> Animal:
    """Create a new animal."""

    db.add(animal)
    db.commit()
    db.refresh(animal)

    return animal


def get_all_animals(
    db: Session
) -> list[Animal]:
    """Return all animals."""

    return db.query(Animal).all()


def get_animal_by_id(
    db: Session,
    animal_id: int
) -> Animal | None:
    """Return one animal by ID."""

    return (
        db.query(Animal)
        .filter(Animal.id == animal_id)
        .first()
    )


def update_animal(
    db: Session,
    animal: Animal,
    animal_data: dict
) -> Animal:
    """Update an existing animal."""

    for field, value in animal_data.items():
        setattr(animal, field, value)

    db.commit()
    db.refresh(animal)

    return animal


def delete_animal(
    db: Session,
    animal: Animal
) -> None:
    """Delete an animal."""

    db.delete(animal)
    db.commit()