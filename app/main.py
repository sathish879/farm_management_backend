from fastapi import FastAPI
from sqlalchemy import text

from sqlalchemy.exc import IntegrityError

from app.core.exceptions import integrity_error_handler


from app.database import engine
from app.routes.farm import router as farm_router
from app.routes.animal import router as animal_router
from app.routes.animal_movement import router as animal_movement_router
from app.routes.feed_type import router as feed_type_router
from app.routes.feed_record import router as feed_record_router
from app.routes.medicine import router as medicine_router
from app.routes.medicine_record import router as medicine_record_router
from app.routes.weight_record import router as weight_record_router
from app.routes.sale import router as sale_router
from app.routes.expense import router as expense_router
from app.routes.income import router as income_router
from app.routes.profit_loss import router as profit_loss_router
from app.routes.dashboard import router as dashboard_router
from app.routes.auth import router as auth_router
from app.routes.user import router as user_router




app = FastAPI()
app.add_exception_handler(
    IntegrityError,
    integrity_error_handler
)

app.include_router(farm_router)
app.include_router(animal_router)
app.include_router(animal_movement_router)
app.include_router(feed_type_router)
app.include_router(feed_record_router)
app.include_router(medicine_router)
app.include_router(medicine_record_router)
app.include_router(weight_record_router)
app.include_router(sale_router)
app.include_router(expense_router)
app.include_router(income_router)
app.include_router(profit_loss_router)
app.include_router(dashboard_router)
app.include_router(auth_router)
app.include_router(user_router)
@app.get("/")
def root():
    """Return a basic message to confirm that FastAPI is running."""

    return {
        "message": "Farm Management API is running"
    }


@app.get("/database-test")
def database_test():
    """Test the connection between FastAPI and PostgreSQL."""

    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database()")
        )

        database_name = result.scalar()

    return {
        "database": database_name,
        "status": "connected",
    }