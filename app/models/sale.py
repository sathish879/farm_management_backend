from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Sale(Base):
    __tablename__ = "sales"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    animal_id: Mapped[int] = mapped_column(
        ForeignKey("animals.id"),
        nullable=False,
        unique=True
    )

    sale_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    buyer_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    buyer_phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    sale_price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    sale_status: Mapped[str] = mapped_column(
        String(30),
        default="COMPLETED",
        nullable=False
    )

    notes: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
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