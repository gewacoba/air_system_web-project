from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemes.users import SUserGet


class STicketAdd(BaseModel):
    user_id: int
    quantity: int
    flight_id: int


class STicketGet(STicketAdd):
    id: int


class STicketPatch(BaseModel):
    user_id: int | None = None
    quantity: int | None = None
    flight_id: int | None = None