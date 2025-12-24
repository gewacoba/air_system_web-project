from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.database.database import Base
from datetime import datetime

if TYPE_CHECKING:
    from app.models.roles import RoleModel


class FlightModel(Base):
    __tablename__ = "flights"

    id: Mapped[int] = mapped_column(primary_key=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    company_id: Mapped[int] = mapped_column(Integer, ForeignKey("air_companies.id"),  nullable=False)
    departure_city_id: Mapped[int] = mapped_column(Integer, ForeignKey("cities.id"), nullable=False)
    landing_city_id: Mapped[int] = mapped_column(Integer, ForeignKey("cities.id"), nullable=False)
    plane_id: Mapped[int] = mapped_column(Integer, ForeignKey("planes.id"), nullable=False)

    cost_of_ticket: Mapped[int] = mapped_column(Integer, nullable = False)
    departure: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    landing: Mapped[datetime] = mapped_column(DateTime, nullable=False)



    