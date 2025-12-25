from app.repositories.cities import CityRepository
from app.schemes.cities import SCityAdd, SCityGet
from app.services.base import BaseService


class CityService(BaseService):
    async def add_city(self, city_data: SCityAdd):
        city = await self.db.cities.add(city_data)
        await self.db.commit()
        return city
    
    async def get_all_cities(self):
        cities = await self.db.cities.get_all()
        return cities
    
    async def get_city(self, city_id: int):
        city = await self.db.cities.get_one_or_none(id=city_id)
        return city
    
    async def update_city(self, city_id: int, city_data: SCityAdd):
        await self.db.cities.edit(city_data, exclude_unset=True, id=city_id)
        await self.db.commit()
    
    async def delete_city(self, city_id: int):
        await self.db.cities.delete(id=city_id)
        await self.db.commit()