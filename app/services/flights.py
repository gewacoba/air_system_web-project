from app.repositories.flights import FlightRepository
from app.schemes.flights import SFlightAdd, SFlightGet
from app.services.base import BaseService
from app.exceptions.base import ObjectNotFoundError


class FlightService(BaseService):
    async def add_flight(self, flight_data: SFlightAdd):
        # Проверяем существование авиакомпании
        company = await self.db.air_companies.get_one_or_none(id=flight_data.company_id)
        if not company:
            raise ObjectNotFoundError(f"Авиакомпания с id {flight_data.company_id} не найдена")
        
        # Проверяем существование города отправления
        departure_city = await self.db.cities.get_one_or_none(id=flight_data.departure_city_id)
        if not departure_city:
            raise ObjectNotFoundError(f"Город отправления с id {flight_data.departure_city_id} не найден")
        
        # Проверяем существование города посадки
        landing_city = await self.db.cities.get_one_or_none(id=flight_data.landing_city_id)
        if not landing_city:
            raise ObjectNotFoundError(f"Город посадки с id {flight_data.landing_city_id} не найден")
        
        # Проверяем существование самолета
        plane = await self.db.planes.get_one_or_none(id=flight_data.plane_id)
        if not plane:
            raise ObjectNotFoundError(f"Самолет с id {flight_data.plane_id} не найден")
        
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
        # Проверяем существование авиакомпании
        if flight_data.company_id is not None:
            company = await self.db.air_companies.get_one_or_none(id=flight_data.company_id)
            if not company:
                raise ObjectNotFoundError(f"Авиакомпания с id {flight_data.company_id} не найдена")
        
        # Проверяем существование города отправления
        if flight_data.departure_city_id is not None:
            departure_city = await self.db.cities.get_one_or_none(id=flight_data.departure_city_id)
            if not departure_city:
                raise ObjectNotFoundError(f"Город отправления с id {flight_data.departure_city_id} не найден")
        
        # Проверяем существование города посадки
        if flight_data.landing_city_id is not None:
            landing_city = await self.db.cities.get_one_or_none(id=flight_data.landing_city_id)
            if not landing_city:
                raise ObjectNotFoundError(f"Город посадки с id {flight_data.landing_city_id} не найден")
        
        # Проверяем существование самолета
        if flight_data.plane_id is not None:
            plane = await self.db.planes.get_one_or_none(id=flight_data.plane_id)
            if not plane:
                raise ObjectNotFoundError(f"Самолет с id {flight_data.plane_id} не найден")
        
        await self.db.flights.edit(flight_data, exclude_unset=True, id=flight_id)
        await self.db.commit()
    
    async def delete_flight(self, flight_id: int):
        await self.db.flights.delete(id=flight_id)
        await self.db.commit()