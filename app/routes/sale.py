from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers.sale import SaleController
from app.core.dependencies import get_db
from app.core.roles import require_authenticated_user
from app.schemas.sale import (
    SaleCreate,
    SaleUpdate,
    SalePatch,
    SaleResponse,
)


router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)

controller = SaleController()


@router.post(
    "/",
    response_model=SaleResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_authenticated_user)]
)
def create_sale(
    data: SaleCreate,
    db: Session = Depends(get_db)
):
    """Create a new sale."""

    return controller.create(
        db,
        data
    )


@router.get(
    "/",
    response_model=list[SaleResponse],
    dependencies=[Depends(require_authenticated_user)]
)
def get_sales(
    db: Session = Depends(get_db)
):
    """Get all sales."""

    return controller.get_all(db)


@router.get(
    "/{sale_id}",
    response_model=SaleResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def get_sale(
    sale_id: int,
    db: Session = Depends(get_db)
):
    """Get a sale by ID."""

    return controller.get_by_id(
        db,
        sale_id
    )


@router.put(
    "/{sale_id}",
    response_model=SaleResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def update_sale(
    sale_id: int,
    data: SaleUpdate,
    db: Session = Depends(get_db)
):
    """Update a sale completely."""

    return controller.update(
        db,
        sale_id,
        data
    )


@router.patch(
    "/{sale_id}",
    response_model=SaleResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def patch_sale(
    sale_id: int,
    data: SalePatch,
    db: Session = Depends(get_db)
):
    """Partially update a sale."""

    return controller.patch(
        db,
        sale_id,
        data
    )


@router.delete(
    "/{sale_id}",
    dependencies=[Depends(require_authenticated_user)]
)
def delete_sale(
    sale_id: int,
    db: Session = Depends(get_db)
):
    """Delete a sale."""

    return controller.delete(
        db,
        sale_id
    )