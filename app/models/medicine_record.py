from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class MedicineRecord(Base):
    __tablename__ = "medicine_records"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    animal_id: Mapped[int] = mapped_column(
        ForeignKey("animals.id"),
        nullable=False
    )

    medicine_id: Mapped[int] = mapped_column(
        ForeignKey("medicines.id"),
        nullable=False
    )

    treatment_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    dosage: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    reason: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    cost: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    veterinarian: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True
    )

    withdrawal_days: Mapped[int | None] = mapped_column(
        nullable=True
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