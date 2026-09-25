from sqlalchemy.orm import Session

from app.models.animal_movement import AnimalMovement


def create_movement(
    db: Session,
    movement: AnimalMovement
) -> AnimalMovement:
    """Create a new animal movement record."""
    db.add(movement)
    db.commit()
    db.refresh(movement)
    return movement


def get_all_movements(db: Session) -> list[AnimalMovement]:
    """Return all animal movement records."""
    return db.query(AnimalMovement).all()


def get_movement_by_id(
    db: Session,
    movement_id: int
) -> AnimalMovement | None:
    """Return one movement by its ID."""
    return (
        db.query(AnimalMovement)
        .filter(AnimalMovement.id == movement_id)
        .first()
    )


def update_movement(
    db: Session,
    movement: AnimalMovement,
    movement_data: dict
) -> AnimalMovement:
    """Update an existing animal movement."""
    for field, value in movement_data.items():
        setattr(movement, field, value)

    db.commit()
    db.refresh(movement)

    return movement


def delete_movement(
    db: Session,
    movement: AnimalMovement
) -> None:
    """Delete an animal movement."""
    db.delete(movement)
    db.commit()