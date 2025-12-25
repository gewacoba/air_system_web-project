from app.models.planes import PlaneModel
from app.schemes.planes import SPlaneGet, SPlaneAdd
from app.repositories.base import BaseRepository


class PlaneRepository(BaseRepository):
    model = PlaneModel
    schema = SPlaneGet