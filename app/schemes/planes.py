from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemes.users import SUserGet


class SPlaneAdd(BaseModel):
    name: str
    seats_quantity: int
    image_url: str


class SPlaneGet(SPlaneAdd):
    id: int


class SPlanePatch(BaseModel):
    name: str | None = None
    seats_quantity: int | None = None
    image_url: str | None = None
