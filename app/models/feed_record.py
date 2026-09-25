from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class FeedRecord(Base):
    __tablename__ = "feed_records"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    animal_id: Mapped[int] = mapped_column(
        ForeignKey("animals.id"),
        nullable=False
    )

    feed_type_id: Mapped[int] = mapped_column(
        ForeignKey("feed_types.id"),
        nullable=False
    )

    feed_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    quantity: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    cost: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
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