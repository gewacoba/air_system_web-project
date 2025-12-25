from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemes.users import SUserGet


class SCityAdd(BaseModel):
    name: str


class SCityGet(SCityAdd):
    id: int


class SCityPatch(BaseModel):
    name: str | None = None