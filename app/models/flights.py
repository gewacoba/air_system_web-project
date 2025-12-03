from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base
from datetime import datetime

if TYPE_CHECKING:
    from app.models.roles import RoleModel


class Airline_ticketModel(Base):
    __tablename__ = "airline_tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    company_id: ...
    departure_city_id: ...
    landing_city_id: ...
    plane_id: ...
    cost_of_ticket: Mapped[int] = mapped_column(Integer, nullable = False)
    departure: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    landing: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    # user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    # quantity: Mapped[int] = mapped_column(Integer, nullable=False)