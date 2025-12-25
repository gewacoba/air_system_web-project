from app.models.cities import CityModel
from app.schemes.cities import SCityGet, SCityAdd
from app.repositories.base import BaseRepository


class CityRepository(BaseRepository):
    model = CityModel
    schema = SCityGet