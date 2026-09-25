from sqlalchemy.orm import Session

from app.services.dashboard import DashboardService


class DashboardController:

    def __init__(self):
        self.service = DashboardService()

    def get_dashboard(
        self,
        db: Session,
        farm_id: int
    ):

        return self.service.get_dashboard(
            db,
            farm_id
        )