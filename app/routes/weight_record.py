from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.weight_record import WeightRecordController
from app.core.dependencies import get_db
from app.core.roles import require_authenticated_user
from app.schemas.weight_record import (
    WeightRecordCreate,
    WeightRecordUpdate,
    WeightRecordPatch,
    WeightRecordResponse,
)


router = APIRouter(
    prefix="/weight-records",
    tags=["Weight Records"]
)

controller = WeightRecordController()


@router.post(
    "/",
    response_model=WeightRecordResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_authenticated_user)]
)
def create_weight_record(
    data: WeightRecordCreate,
    db: Session = Depends(get_db)
):
    """Create a new weight record."""

    return controller.create(
        db,
        data
    )


@router.get(
    "/",
    response_model=list[WeightRecordResponse],
    dependencies=[Depends(require_authenticated_user)]
)
def get_weight_records(
    db: Session = Depends(get_db)
):
    """Get all weight records."""

    return controller.get_all(db)


@router.get(
    "/{weight_record_id}",
    response_model=WeightRecordResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def get_weight_record(
    weight_record_id: int,
    db: Session = Depends(get_db)
):
    """Get a weight record by ID."""

    return controller.get_by_id(
        db,
        weight_record_id
    )


@router.put(
    "/{weight_record_id}",
    response_model=WeightRecordResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def update_weight_record(
    weight_record_id: int,
    data: WeightRecordUpdate,
    db: Session = Depends(get_db)
):
    """Update a weight record completely."""

    return controller.update(
        db,
        weight_record_id,
        data
    )


@router.patch(
    "/{weight_record_id}",
    response_model=WeightRecordResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def patch_weight_record(
    weight_record_id: int,
    data: WeightRecordPatch,
    db: Session = Depends(get_db)
):
    """Partially update a weight record."""

    return controller.patch(
        db,
        weight_record_id,
        data
    )


@router.delete(
    "/{weight_record_id}",
    dependencies=[Depends(require_authenticated_user)]
)
def delete_weight_record(
    weight_record_id: int,
    db: Session = Depends(get_db)
):
    """Delete a weight record."""

    return controller.delete(
        db,
        weight_record_id
    )