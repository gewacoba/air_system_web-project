from fastapi import APIRouter

from app.api.dependencies import DBDep
from app.schemes.cities import SCityAdd, SCityGet
from app.services.cities import CityService

router = APIRouter(prefix="/cities", tags=["Управление городами"])


@router.post("/", summary="Создание нового города")
async def create_new_city(
    city_data: SCityAdd,
    db: DBDep,
) -> dict[str, str]:
    await CityService(db).add_city(city_data)
    return {"status": "OK"}


@router.get("/", summary="Получение списка городов")
async def get_all_cities(
    db: DBDep,
) -> list[SCityGet]:
    cities = await CityService(db).get_all_cities()
    return cities


@router.get("/{id}", summary="Получение конкретного города")
async def get_city(
    db: DBDep,
    id: int,
) -> SCityGet | None:
    city = await CityService(db).get_city(id)
    return city


@router.put("/{id}", summary="Изменение конкретного города")
async def update_city(
    db: DBDep,
    city_data: SCityAdd,
    id: int,
) -> dict[str, str]:
    await CityService(db).update_city(id, city_data)
    return {"status": "OK"}


@router.delete("/{id}", summary="Удаление конкретного города")
async def delete_city(
    db: DBDep,
    id: int,
) -> dict[str, str]:
    await CityService(db).delete_city(id)
    return {"status": "OK"}