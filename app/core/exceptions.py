from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError


async def integrity_error_handler(
    request: Request,
    exc: IntegrityError
):
    """
    Handle database integrity errors globally.

    Examples:
    - Duplicate unique value
    - Foreign key violation
    - Other database constraint violations
    """

    error_message = str(exc.orig)

    if "duplicate key value" in error_message:
        detail = "Duplicate value already exists."

    elif "foreign key constraint" in error_message:
        detail = "This record cannot be changed or deleted because it is being used by another record."

    else:
        detail = "Database constraint violation."

    return JSONResponse(
        status_code=400,
        content={
            "detail": detail
        }
    )