from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers import farm as farm_controller
from app.database import SessionLocal
from app.schemas.farm import (
    FarmCreate,
    FarmPatch,
    FarmResponse,
    FarmUpdate,
)


router = APIRouter(
    prefix="/farms",
    tags=["Farms"]
)


def get_db():
    """Create and close a database session for each request."""

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# CREATE
@router.post("/", response_model=FarmResponse)
def create_farm(
    farm_data: FarmCreate,
    db: Session = Depends(get_db)
):
    """Create a new farm."""

    return farm_controller.create_farm(
        db,
        farm_data
    )


# READ ALL
@router.get("/", response_model=list[FarmResponse])
def get_all_farms(
    db: Session = Depends(get_db)
):
    """Get all farms."""

    return farm_controller.get_all_farms(db)


# READ ONE
@router.get("/{farm_id}", response_model=FarmResponse)
def get_farm_by_id(
    farm_id: int,
    db: Session = Depends(get_db)
):
    """Get one farm by ID."""

    farm = farm_controller.get_farm_by_id(
        db,
        farm_id
    )

    if farm is None:
        raise HTTPException(
            status_code=404,
            detail="Farm not found"
        )

    return farm


# PUT - FULL UPDATE
@router.put("/{farm_id}", response_model=FarmResponse)
def update_farm(
    farm_id: int,
    farm_data: FarmUpdate,
    db: Session = Depends(get_db)
):
    """Fully update a farm."""

    farm = farm_controller.update_farm(
        db,
        farm_id,
        farm_data
    )

    if farm is None:
        raise HTTPException(
            status_code=404,
            detail="Farm not found"
        )

    return farm


# PATCH - PARTIAL UPDATE
@router.patch("/{farm_id}", response_model=FarmResponse)
def patch_farm(
    farm_id: int,
    farm_data: FarmPatch,
    db: Session = Depends(get_db)
):
    """Partially update a farm."""

    farm = farm_controller.patch_farm(
        db,
        farm_id,
        farm_data
    )

    if farm is None:
        raise HTTPException(
            status_code=404,
            detail="Farm not found"
        )

    return farm


# DELETE
@router.delete("/{farm_id}")
def delete_farm(
    farm_id: int,
    db: Session = Depends(get_db)
):
    """Delete a farm."""

    deleted = farm_controller.delete_farm(
        db,
        farm_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Farm not found"
        )

    return {
        "message": "Farm deleted successfully"
    }