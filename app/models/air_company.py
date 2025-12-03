from typing import TYPE_CHECKING

from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.roles import RoleModel


class Air_companyModel(Base):
    __tablename__ = "air_companies"
    name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)