from typing import TYPE_CHECKING

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.roles import RoleModel


class PlaneModel(Base):
    __tablename__ = "planes"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    seats_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    image_url: Mapped[str] = mapped_column(String(2048), nullable=False)

    