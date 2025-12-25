from app.database.database import async_session_maker
from app.repositories.planes import PlaneRepository
from app.repositories.roles import RolesRepository
from app.repositories.users import UsersRepository
from app.repositories.air_companies import AirCompanyRepository


class DBManager:
    def __init__(self, session_factory: async_session_maker):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()
        # TODO Добавить сюда созданные репозитории
        # Пример:
        self.users = UsersRepository(self.session)
        self.roles = RolesRepository(self.session)
        self.planes = PlaneRepository(self.session)
        self.air_companies = AirCompanyRepository(self.session)
        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()
