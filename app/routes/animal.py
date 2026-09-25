from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers import animal as animal_controller
from app.core.dependencies import get_db
from app.core.roles import require_authenticated_user
from app.schemas.animal import (
    AnimalCreate,
    AnimalPatch,
    AnimalResponse,
    AnimalUpdate,
)

router = APIRouter(
    prefix="/animals",
    tags=["Animals"]
)


@router.post(
    "/",
    response_model=AnimalResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def create_animal(
    animal_data: AnimalCreate,
    db: Session = Depends(get_db)
):
    return animal_controller.create_animal(db, animal_data)


@router.get(
    "/",
    response_model=list[AnimalResponse],
    dependencies=[Depends(require_authenticated_user)]
)
def get_animals(
    db: Session = Depends(get_db)
):
    return animal_controller.get_animals(db)


@router.get(
    "/{animal_id}",
    response_model=AnimalResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def get_animal(
    animal_id: int,
    db: Session = Depends(get_db)
):
    return animal_controller.get_animal(db, animal_id)


@router.put(
    "/{animal_id}",
    response_model=AnimalResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def update_animal(
    animal_id: int,
    animal_data: AnimalUpdate,
    db: Session = Depends(get_db)
):
    return animal_controller.update_animal(
        db,
        animal_id,
        animal_data
    )


@router.patch(
    "/{animal_id}",
    response_model=AnimalResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def patch_animal(
    animal_id: int,
    animal_data: AnimalPatch,
    db: Session = Depends(get_db)
):
    return animal_controller.patch_animal(
        db,
        animal_id,
        animal_data
    )


@router.delete(
    "/{animal_id}",
    dependencies=[Depends(require_authenticated_user)]
)
def delete_animal(
    animal_id: int,
    db: Session = Depends(get_db)
):
    return animal_controller.delete_animal(db, animal_id)