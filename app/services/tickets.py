from app.repositories.tickets import TicketRepository
from app.schemes.tickets import STicketAdd, STicketGet
from app.services.base import BaseService
from app.exceptions.base import ObjectNotFoundError


class TicketService(BaseService):
    async def add_ticket(self, ticket_data: STicketAdd):
        # Проверяем существование пользователя
        user = await self.db.users.get_one_or_none(id=ticket_data.user_id)
        if not user:
            raise ObjectNotFoundError(f"Пользователь с id {ticket_data.user_id} не найден")
        
        # Проверяем существование рейса
        flight = await self.db.flights.get_one_or_none(id=ticket_data.flight_id)
        if not flight:
            raise ObjectNotFoundError(f"Рейс с id {ticket_data.flight_id} не найден")
        
        ticket = await self.db.tickets.add(ticket_data)
        await self.db.commit()
        return ticket
    
    async def get_all_tickets(self):
        tickets = await self.db.tickets.get_all()
        return tickets
    
    async def get_ticket(self, ticket_id: int):
        ticket = await self.db.tickets.get_one_or_none(id=ticket_id)
        return ticket
    
    async def update_ticket(self, ticket_id: int, ticket_data: STicketAdd):
        # Проверяем существование пользователя
        if ticket_data.user_id is not None:
            user = await self.db.users.get_one_or_none(id=ticket_data.user_id)
            if not user:
                raise ObjectNotFoundError(f"Пользователь с id {ticket_data.user_id} не найден")
        
        # Проверяем существование рейса
        if ticket_data.flight_id is not None:
            flight = await self.db.flights.get_one_or_none(id=ticket_data.flight_id)
            if not flight:
                raise ObjectNotFoundError(f"Рейс с id {ticket_data.flight_id} не найден")
        
        await self.db.tickets.edit(ticket_data, exclude_unset=True, id=ticket_id)
        await self.db.commit()
    
    async def delete_ticket(self, ticket_id: int):
        await self.db.tickets.delete(id=ticket_id)
        await self.db.commit()