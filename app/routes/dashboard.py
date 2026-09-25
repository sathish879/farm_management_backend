from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers.dashboard import DashboardController
from app.core.dependencies import get_db
from app.core.roles import require_authenticated_user
from app.schemas.dashboard import DashboardResponse


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

controller = DashboardController()


@router.get(
    "/{farm_id}",
    response_model=DashboardResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def get_dashboard(
    farm_id: int,
    db: Session = Depends(get_db)
):
    """Get dashboard information for a farm."""

    return controller.get_dashboard(
        db,
        farm_id
    )