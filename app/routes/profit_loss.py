from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers.profit_loss import ProfitLossController
from app.core.dependencies import get_db
from app.core.roles import require_authenticated_user
from app.schemas.profit_loss import ProfitLossResponse


router = APIRouter(
    prefix="/profit-loss",
    tags=["Profit & Loss"]
)

controller = ProfitLossController()


@router.get(
    "/{farm_id}",
    response_model=ProfitLossResponse,
    dependencies=[Depends(require_authenticated_user)]
)
def get_profit_loss(
    farm_id: int,
    db: Session = Depends(get_db)
):
    """Get profit and loss for a farm."""

    return controller.get_profit_loss(
        db,
        farm_id
    )