from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class AnimalMovement(Base):
    __tablename__ = "animal_movements"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    animal_id: Mapped[int] = mapped_column(
        ForeignKey("animals.id"),
        nullable=False
    )

    movement_type: Mapped[str] = mapped_column(
        String(10),
        nullable=False
    )

    movement_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    reason: Mapped[str] = mapped_column(
        String(100),
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