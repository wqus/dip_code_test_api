from sqlalchemy import Integer, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped
from app.db.base import Base
from datetime import datetime


class Stats(Base):
    __tablename__ = "stats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    device_id: Mapped[int] = mapped_column(ForeignKey("devices.id"), index=True)
    x: Mapped[float] = mapped_column(Float)
    y: Mapped[float] = mapped_column(Float)
    z: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), index=True)
