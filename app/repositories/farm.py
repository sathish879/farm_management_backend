from sqlalchemy.orm import Session

from app.models.farm import Farm


def create_farm(db: Session, farm: Farm) -> Farm:
    """Save a new farm in the database."""

    db.add(farm)
    db.commit()
    db.refresh(farm)

    return farm


def get_all_farms(db: Session) -> list[Farm]:
    """Get all farms from the database."""

    return db.query(Farm).all()


def get_farm_by_id(db: Session, farm_id: int) -> Farm | None:
    """Get one farm by its ID."""

    return db.query(Farm).filter(Farm.id == farm_id).first()


def update_farm(
    db: Session,
    farm: Farm,
    farm_data: dict
) -> Farm:
    """Update farm fields in the database."""

    for field, value in farm_data.items():
        setattr(farm, field, value)

    db.commit()
    db.refresh(farm)

    return farm


def delete_farm(db: Session, farm: Farm) -> None:
    """Delete a farm from the database."""

    db.delete(farm)
    db.commit()