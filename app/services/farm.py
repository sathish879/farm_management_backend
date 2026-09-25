from sqlalchemy.orm import Session

from app.models.farm import Farm
from app.repositories import farm as farm_repository


def create_farm(db: Session, farm_data) -> Farm:
    """Create a new farm."""

    farm = Farm(
        farm_code=farm_data.farm_code,
        name=farm_data.name,
        location=farm_data.location,
        owner_name=farm_data.owner_name,
        phone=farm_data.phone,
    )

    return farm_repository.create_farm(db, farm)


def get_all_farms(db: Session) -> list[Farm]:
    """Get all farms."""

    return farm_repository.get_all_farms(db)


def get_farm_by_id(db: Session, farm_id: int) -> Farm | None:
    """Get one farm by ID."""

    return farm_repository.get_farm_by_id(db, farm_id)


def update_farm(db: Session, farm_id: int, farm_data) -> Farm | None:
    """Fully update a farm."""

    farm = farm_repository.get_farm_by_id(db, farm_id)

    if farm is None:
        return None

    data = farm_data.model_dump()

    return farm_repository.update_farm(db, farm, data)


def patch_farm(db: Session, farm_id: int, farm_data) -> Farm | None:
    """Partially update a farm."""

    farm = farm_repository.get_farm_by_id(db, farm_id)

    if farm is None:
        return None

    data = farm_data.model_dump(exclude_unset=True)

    return farm_repository.update_farm(db, farm, data)


def delete_farm(db: Session, farm_id: int) -> bool:
    """Delete a farm."""

    farm = farm_repository.get_farm_by_id(db, farm_id)

    if farm is None:
        return False

    farm_repository.delete_farm(db, farm)

    return True