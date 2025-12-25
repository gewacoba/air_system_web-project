from app.repositories.planes import PlaneRepository
from app.schemes.planes import SPlaneAdd, SPlaneGet
from app.services.base import BaseService


class PlaneService(BaseService):
    async def add_plane(self, plane_data: SPlaneAdd):
        plane = await self.db.planes.add(plane_data)
        await self.db.commit()
        return plane
    
    async def get_all_planes(self):
        planes = await self.db.planes.get_all()
        return planes
    
    async def get_plane(self, plane_id: int):
       
        plane = await self.db.planes.get_one_or_none(id=plane_id)
        return plane
    
    async def update_plane(self, plane_id: int, plane_data: SPlaneAdd):

       await self.db.planes.edit(plane_data, exclude_unset=True, id=plane_id)
       await self.db.commit()
    
    async def delete_plane(self, plane_id: int):
      
        await self.db.planes.delete(id=plane_id)
        await self.db.commit()