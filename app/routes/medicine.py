from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.medicine import MedicineController
from app.core.dependencies import get_db
from app.core.roles import require_authenticated_user
from app.schemas.medicine import (
    MedicineCreate,
    MedicineUpdate,
    MedicinePatch,
    MedicineResponse,
)


router = APIRouter(
    prefix="/medicines",
    tags=["Medicines"]
)

controller = MedicineController()


@router.post(
    "/",
    response_model=MedicineResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_authenticated_user)]
)
def create_medicine(
    data: MedicineCreate,
    db: Session = Depends(get_db)
):
    """Create a new medicine."""

    return controller.create(
        db,
        data
    )


@router.get(
    "/",
    response_model=list[MedicineResponse],
    dependencies=[Depends(require_authenticated_user)]
)
def get_medicines(
    db: Session = Depends(get_db)
):
    """Get all medicines."""

    return controller.get_all(db)


@router.get(
    "/{medicine_id}",
    response_model=MedicineResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def get_medicine(
    medicine_id: int,
    db: Session = Depends(get_db)
):
    """Get a medicine by ID."""

    return controller.get_by_id(
        db,
        medicine_id
    )


@router.put(
    "/{medicine_id}",
    response_model=MedicineResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def update_medicine(
    medicine_id: int,
    data: MedicineUpdate,
    db: Session = Depends(get_db)
):
    """Update a medicine completely."""

    return controller.update(
        db,
        medicine_id,
        data
    )


@router.patch(
    "/{medicine_id}",
    response_model=MedicineResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def patch_medicine(
    medicine_id: int,
    data: MedicinePatch,
    db: Session = Depends(get_db)
):
    """Partially update a medicine."""

    return controller.patch(
        db,
        medicine_id,
        data
    )


@router.delete(
    "/{medicine_id}",
    dependencies=[Depends(require_authenticated_user)]
)
def delete_medicine(
    medicine_id: int,
    db: Session = Depends(get_db)
):
    """Delete a medicine."""

    return controller.delete(
        db,
        medicine_id
    )