from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers import animal_movement as movement_controller
from app.core.dependencies import get_db
from app.core.roles import require_authenticated_user
from app.schemas.animal_movement import (
    AnimalMovementCreate,
    AnimalMovementPatch,
    AnimalMovementResponse,
    AnimalMovementUpdate,
)


router = APIRouter(
    prefix="/animal-movements",
    tags=["Animal Movements"]
)


@router.post(
    "/",
    response_model=AnimalMovementResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def create_movement(
    movement_data: AnimalMovementCreate,
    db: Session = Depends(get_db)
):
    """Create a new animal movement."""

    return movement_controller.create_movement(
        db,
        movement_data
    )


@router.get(
    "/",
    response_model=list[AnimalMovementResponse],
    dependencies=[Depends(require_authenticated_user)]
)
def get_all_movements(
    db: Session = Depends(get_db)
):
    """Get all animal movements."""

    return movement_controller.get_all_movements(db)


@router.get(
    "/{movement_id}",
    response_model=AnimalMovementResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def get_movement_by_id(
    movement_id: int,
    db: Session = Depends(get_db)
):
    """Get an animal movement by ID."""

    movement = movement_controller.get_movement_by_id(
        db,
        movement_id
    )

    if movement is None:
        raise HTTPException(
            status_code=404,
            detail="Animal movement not found"
        )

    return movement


@router.put(
    "/{movement_id}",
    response_model=AnimalMovementResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def update_movement(
    movement_id: int,
    movement_data: AnimalMovementUpdate,
    db: Session = Depends(get_db)
):
    """Update an animal movement completely."""

    movement = movement_controller.update_movement(
        db,
        movement_id,
        movement_data
    )

    if movement is None:
        raise HTTPException(
            status_code=404,
            detail="Animal movement not found"
        )

    return movement


@router.patch(
    "/{movement_id}",
    response_model=AnimalMovementResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def patch_movement(
    movement_id: int,
    movement_data: AnimalMovementPatch,
    db: Session = Depends(get_db)
):
    """Partially update an animal movement."""

    movement = movement_controller.patch_movement(
        db,
        movement_id,
        movement_data
    )

    if movement is None:
        raise HTTPException(
            status_code=404,
            detail="Animal movement not found"
        )

    return movement


@router.delete(
    "/{movement_id}",
    dependencies=[Depends(require_authenticated_user)]
)
def delete_movement(
    movement_id: int,
    db: Session = Depends(get_db)
):
    """Delete an animal movement."""

    deleted = movement_controller.delete_movement(
        db,
        movement_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Animal movement not found"
        )

    return {
        "message": "Animal movement deleted successfully"
    }
    