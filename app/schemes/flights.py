from typing import TYPE_CHECKING
from datetime import datetime

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemes.users import SUserGet


class SFlightAdd(BaseModel):
    is_active: bool = True
    company_id: int
    departure_city_id: int
    landing_city_id: int
    plane_id: int
    cost_of_ticket: int
    departure: datetime
    landing: datetime


class SFlightGet(SFlightAdd):
    id: int


class SFlightPatch(BaseModel):
    is_active: bool | None = None
    company_id: int | None = None
    departure_city_id: int | None = None
    landing_city_id: int | None = None
    plane_id: int | None = None
    cost_of_ticket: int | None = None
    departure: datetime | None = None
    landing: datetime | None = None