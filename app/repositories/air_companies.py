from app.models.air_companies import Air_companyModel
from app.schemes.air_companies import SAirCompanyGet, SAirCompanyAdd
from app.repositories.base import BaseRepository


class AirCompanyRepository(BaseRepository):
    model = Air_companyModel
    schema = SAirCompanyGet