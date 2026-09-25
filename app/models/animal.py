from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Animal(Base):
    __tablename__ = "animals"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    animal_code: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    farm_id: Mapped[int] = mapped_column(
        ForeignKey("farms.id"),
        nullable=False
    )

    animal_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    breed: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    gender: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    date_of_birth: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    purchase_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    purchase_price: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="ACTIVE",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )