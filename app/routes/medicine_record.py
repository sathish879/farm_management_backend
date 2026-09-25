from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.medicine_record import MedicineRecordController
from app.core.dependencies import get_db
from app.core.roles import require_authenticated_user
from app.schemas.medicine_record import (
    MedicineRecordCreate,
    MedicineRecordUpdate,
    MedicineRecordPatch,
    MedicineRecordResponse,
)


router = APIRouter(
    prefix="/medicine-records",
    tags=["Medicine Records"]
)

controller = MedicineRecordController()


@router.post(
    "/",
    response_model=MedicineRecordResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_authenticated_user)]
)
def create_medicine_record(
    data: MedicineRecordCreate,
    db: Session = Depends(get_db)
):
    """Create a new medicine record."""

    return controller.create(
        db,
        data
    )


@router.get(
    "/",
    response_model=list[MedicineRecordResponse],
    dependencies=[Depends(require_authenticated_user)]
)
def get_medicine_records(
    db: Session = Depends(get_db)
):
    """Get all medicine records."""

    return controller.get_all(db)


@router.get(
    "/{medicine_record_id}",
    response_model=MedicineRecordResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def get_medicine_record(
    medicine_record_id: int,
    db: Session = Depends(get_db)
):
    """Get a medicine record by ID."""

    return controller.get_by_id(
        db,
        medicine_record_id
    )


@router.put(
    "/{medicine_record_id}",
    response_model=MedicineRecordResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def update_medicine_record(
    medicine_record_id: int,
    data: MedicineRecordUpdate,
    db: Session = Depends(get_db)
):
    """Update a medicine record completely."""

    return controller.update(
        db,
        medicine_record_id,
        data
    )


@router.patch(
    "/{medicine_record_id}",
    response_model=MedicineRecordResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def patch_medicine_record(
    medicine_record_id: int,
    data: MedicineRecordPatch,
    db: Session = Depends(get_db)
):
    """Partially update a medicine record."""

    return controller.patch(
        db,
        medicine_record_id,
        data
    )


@router.delete(
    "/{medicine_record_id}",
    dependencies=[Depends(require_authenticated_user)]
)
def delete_medicine_record(
    medicine_record_id: int,
    db: Session = Depends(get_db)
):
    """Delete a medicine record."""

    return controller.delete(
        db,
        medicine_record_id
    )