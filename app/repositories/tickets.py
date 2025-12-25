from app.models.tickets import TicketModel
from app.schemes.tickets import STicketGet, STicketAdd
from app.repositories.base import BaseRepository


class TicketRepository(BaseRepository):
    model = TicketModel
    schema = STicketGet