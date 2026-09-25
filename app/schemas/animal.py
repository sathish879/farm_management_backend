from datetime import date, datetime
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict, field_validator, model_validator


class AnimalCreate(BaseModel):
    animal_code: str
    farm_id: int
    animal_type: str
    breed: str
    gender: Literal["Male", "Female"]
    date_of_birth: date | None = None
    purchase_date: date | None = None
    purchase_price: Decimal | None = None
    status: Literal["ACTIVE", "OUT", "SOLD"] = "ACTIVE"

    @field_validator("purchase_price")
    @classmethod
    def validate_purchase_price(cls, value):
        """Ensure purchase price is not negative."""

        if value is not None and value < 0:
            raise ValueError("Purchase price cannot be negative")

        return value

    @model_validator(mode="after")
    def validate_dates(self):
        """Validate animal birth and purchase dates."""

        today = date.today()

        if self.date_of_birth and self.date_of_birth > today:
            raise ValueError("Date of birth cannot be in the future")

        if self.purchase_date and self.purchase_date > today:
            raise ValueError("Purchase date cannot be in the future")

        if (
            self.date_of_birth
            and self.purchase_date
            and self.purchase_date < self.date_of_birth
        ):
            raise ValueError(
                "Purchase date cannot be before date of birth"
            )

        return self


class AnimalUpdate(BaseModel):
    animal_code: str
    farm_id: int
    animal_type: str
    breed: str
    gender: Literal["Male", "Female"]
    date_of_birth: date | None = None
    purchase_date: date | None = None
    purchase_price: Decimal | None = None
    status: Literal["ACTIVE", "OUT", "SOLD"]

    @field_validator("purchase_price")
    @classmethod
    def validate_purchase_price(cls, value):
        """Ensure purchase price is not negative."""

        if value is not None and value < 0:
            raise ValueError("Purchase price cannot be negative")

        return value

    @model_validator(mode="after")
    def validate_dates(self):
        """Validate animal birth and purchase dates."""

        today = date.today()

        if self.date_of_birth and self.date_of_birth > today:
            raise ValueError("Date of birth cannot be in the future")

        if self.purchase_date and self.purchase_date > today:
            raise ValueError("Purchase date cannot be in the future")

        if (
            self.date_of_birth
            and self.purchase_date
            and self.purchase_date < self.date_of_birth
        ):
            raise ValueError(
                "Purchase date cannot be before date of birth"
            )

        return self


class AnimalPatch(BaseModel):
    animal_code: str | None = None
    farm_id: int | None = None
    animal_type: str | None = None
    breed: str | None = None
    gender: Literal["Male", "Female"] | None = None
    date_of_birth: date | None = None
    purchase_date: date | None = None
    purchase_price: Decimal | None = None
    status: Literal["ACTIVE", "OUT", "SOLD"] | None = None

    @field_validator("purchase_price")
    @classmethod
    def validate_purchase_price(cls, value):
        """Ensure purchase price is not negative."""

        if value is not None and value < 0:
            raise ValueError("Purchase price cannot be negative")

        return value

    @model_validator(mode="after")
    def validate_dates(self):
        """Validate provided dates."""

        today = date.today()

        if self.date_of_birth and self.date_of_birth > today:
            raise ValueError("Date of birth cannot be in the future")

        if self.purchase_date and self.purchase_date > today:
            raise ValueError("Purchase date cannot be in the future")

        if (
            self.date_of_birth
            and self.purchase_date
            and self.purchase_date < self.date_of_birth
        ):
            raise ValueError(
                "Purchase date cannot be before date of birth"
            )

        return self


class AnimalResponse(BaseModel):
    id: int
    animal_code: str
    farm_id: int
    animal_type: str
    breed: str
    gender: str
    date_of_birth: date | None
    purchase_date: date | None
    purchase_price: Decimal | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)