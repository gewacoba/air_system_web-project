from app.repositories.air_companies import AirCompanyRepository
from app.schemes.air_companies import SAirCompanyAdd, SAirCompanyGet, SAirCompanyPatch
from app.services.base import BaseService


class AirCompanyService(BaseService):
    async def add_air_company(self, air_company_data: SAirCompanyAdd):
        air_company = await self.db.air_companies.add(air_company_data)
        await self.db.commit()
        return air_company
    
    async def get_all_air_companies(self):
        air_companies = await self.db.air_companies.get_all()
        return air_companies
    
    async def get_air_company(self, air_company_id: int):
       
        air_company = await self.db.air_companies.get_one_or_none(id=air_company_id)
        return air_company
    
    async def update_air_company(self, air_company_id: int, air_company_data: SAirCompanyPatch):
 
       await self.db.air_companies.edit(air_company_data, exclude_unset=True, id=air_company_id)
       await self.db.commit()
    
    async def delete_air_company(self, air_company_id: int):
       
        await self.db.air_companies.delete(id=air_company_id)
        await self.db.commit()