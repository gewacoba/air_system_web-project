from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemes.users import SUserGet


class SAirCompanyAdd(BaseModel):
    name: str


class SAirCompanyGet(SAirCompanyAdd):
    id: int


class SAirCompanyPatch(BaseModel):
    name: str | None = None