from sqlalchemy.orm import Session

from app.schemas.farm import FarmCreate, FarmPatch, FarmUpdate
from app.services import farm as farm_service


def create_farm(db: Session, farm_data: FarmCreate):
    """Handle farm creation."""

    return farm_service.create_farm(db, farm_data)


def get_all_farms(db: Session):
    """Handle getting all farms."""

    return farm_service.get_all_farms(db)


def get_farm_by_id(db: Session, farm_id: int):
    """Handle getting one farm."""

    return farm_service.get_farm_by_id(db, farm_id)


def update_farm(
    db: Session,
    farm_id: int,
    farm_data: FarmUpdate
):
    """Handle full farm update."""

    return farm_service.update_farm(
        db,
        farm_id,
        farm_data
    )


def patch_farm(
    db: Session,
    farm_id: int,
    farm_data: FarmPatch
):
    """Handle partial farm update."""

    return farm_service.patch_farm(
        db,
        farm_id,
        farm_data
    )


def delete_farm(db: Session, farm_id: int):
    """Handle farm deletion."""

    return farm_service.delete_farm(db, farm_id)