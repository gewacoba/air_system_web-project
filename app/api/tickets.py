from fastapi import APIRouter

from app.api.dependencies import DBDep
from app.schemes.tickets import STicketAdd, STicketGet
from app.services.tickets import TicketService

router = APIRouter(prefix="/tickets", tags=["Управление билетами"])


@router.post("/", summary="Создание нового билета")
async def create_new_ticket(
    ticket_data: STicketAdd,
    db: DBDep,
) -> dict[str, str]:
    await TicketService(db).add_ticket(ticket_data)
    return {"status": "OK"}


@router.get("/", summary="Получение списка билетов")
async def get_all_tickets(
    db: DBDep,
) -> list[STicketGet]:
    tickets = await TicketService(db).get_all_tickets()
    return tickets


@router.get("/{id}", summary="Получение конкретного билета")
async def get_ticket(
    db: DBDep,
    id: int,
) -> STicketGet | None:
    ticket = await TicketService(db).get_ticket(id)
    return ticket


@router.put("/{id}", summary="Изменение конкретного билета")
async def update_ticket(
    db: DBDep,
    ticket_data: STicketAdd,
    id: int,
) -> dict[str, str]:
    await TicketService(db).update_ticket(id, ticket_data)
    return {"status": "OK"}


@router.delete("/{id}", summary="Удаление конкретного билета")
async def delete_ticket(
    db: DBDep,
    id: int,
) -> dict[str, str]:
    await TicketService(db).delete_ticket(id)
    return {"status": "OK"}