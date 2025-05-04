"""Flask SQLAlchemy model definitions."""

from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column

from . import db


class Payload(db.Model):
  __tablename__ = "payloads"

  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  data: Mapped[dict[str, any]] = mapped_column(JSON, nullable=False)
  created_at: Mapped[datetime] = mapped_column(
      DateTime, default=lambda: datetime.now(timezone.utc)
  )
