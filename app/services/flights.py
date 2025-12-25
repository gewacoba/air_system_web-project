from app.repositories.flights import FlightRepository
from app.schemes.flights import SFlightAdd, SFlightGet
from app.services.base import BaseService


class FlightService(BaseService):
    async def add_flight(self, flight_data: SFlightAdd):
        flight = await self.db.flights.add(flight_data)
        await self.db.commit()
        return flight
    
    async def get_all_flights(self):
        flights = await self.db.flights.get_all()
        return flights
    
    async def get_flight(self, flight_id: int):
        flight = await self.db.flights.get_one_or_none(id=flight_id)
        return flight
    
    async def update_flight(self, flight_id: int, flight_data: SFlightAdd):
        await self.db.flights.edit(flight_data, exclude_unset=True, id=flight_id)
        await self.db.commit()
    
    async def delete_flight(self, flight_id: int):
        await self.db.flights.delete(id=flight_id)
        await self.db.commit()