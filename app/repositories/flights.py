from app.models.flights import FlightModel
from app.schemes.flights import SFlightGet, SFlightAdd
from app.repositories.base import BaseRepository


class FlightRepository(BaseRepository):
    model = FlightModel
    schema = SFlightGet