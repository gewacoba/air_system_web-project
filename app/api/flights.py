from fastapi import APIRouter

from app.api.dependencies import DBDep
from app.schemes.flights import SFlightAdd, SFlightGet
from app.services.flights import FlightService
from app.exceptions.base import ObjectNotFoundError

router = APIRouter(prefix="/flights", tags=["Управление рейсами"])


@router.post("/", summary="Создание нового рейса")
async def create_new_flight(
    flight_data: SFlightAdd,
    db: DBDep,
) -> dict[str, str]:
    try:
        await FlightService(db).add_flight(flight_data)
    except ObjectNotFoundError as e:
        raise e
    return {"status": "OK"}


@router.get("/", summary="Получение списка рейсов")
async def get_all_flights(
    db: DBDep,
) -> list[SFlightGet]:
    flights = await FlightService(db).get_all_flights()
    return flights


@router.get("/{id}", summary="Получение конкретного рейса")
async def get_flight(
    db: DBDep,
    id: int,
) -> SFlightGet | None:
    flight = await FlightService(db).get_flight(id)
    return flight


@router.put("/{id}", summary="Изменение конкретного рейса")
async def update_flight(
    db: DBDep,
    flight_data: SFlightAdd,
    id: int,
) -> dict[str, str]:
    try:
        await FlightService(db).update_flight(id, flight_data)
    except ObjectNotFoundError as e:
        raise e
    return {"status": "OK"}


@router.delete("/{id}", summary="Удаление конкретного рейса")
async def delete_flight(
    db: DBDep,
    id: int,
) -> dict[str, str]:
    await FlightService(db).delete_flight(id)
    return {"status": "OK"}