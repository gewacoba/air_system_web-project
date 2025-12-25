from fastapi import APIRouter

from app.api.dependencies import DBDep
from app.schemes.air_companies import SAirCompanyAdd, SAirCompanyGet
from app.services.air_companies import AirCompanyService

router = APIRouter(prefix="/air-companies", tags=["Управление авиакомпаниями"])


@router.post("/", summary="Создание новой авиакомпании")
async def create_new_air_company(
    air_company_data: SAirCompanyAdd,
    db: DBDep,
) -> dict[str, str]:
    await AirCompanyService(db).add_air_company(air_company_data)
    return {"status": "OK"}


@router.get("/", summary="Получение списка авиакомпаний")
async def get_all_air_companies(
    db: DBDep,
) -> list[SAirCompanyGet]:
    air_companies = await AirCompanyService(db).get_all_air_companies()
    return air_companies


@router.get("/{id}", summary="Получение конкретной авиакомпании")
async def get_air_company(
    db: DBDep,
    id: int,
) -> SAirCompanyGet | None:
    air_company = await AirCompanyService(db).get_air_company(id)
    return air_company


@router.put("/{id}", summary="Изменение конкретной авиакомпании")
async def update_air_company(
    db: DBDep,
    air_company_data: SAirCompanyAdd,
    id: int,
) -> dict[str, str]:
    await AirCompanyService(db).update_air_company(id, air_company_data)
    return {"status": "OK"}


@router.delete("/{id}", summary="Удаление конкретной авиакомпании")
async def delete_air_company(
    db: DBDep,
    id: int,
) -> dict[str, str]:
    await AirCompanyService(db).delete_air_company(id)
    return {"status": "OK"}