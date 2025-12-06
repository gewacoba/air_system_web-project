from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.roles import RoleModel


class TicketModel(Base):
    __tablename__ = "ticekts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    flight: Mapped[int] = mapped_column(ForeignKey("flights.id"), nullable=False)