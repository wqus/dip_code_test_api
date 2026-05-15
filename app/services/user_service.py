from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.repositories.user_repo import UserRepository


class UserService:
    def __init__(self, session: AsyncSession):
        self.repo = UserRepository(session)

    async def create_user(self, name: str) -> User:
        return await self.repo.create_user(name)

    async def get_user_by_id(self, user_id: int) -> User | None:
        return await self.repo.get_user_by_id(user_id)

    async def get_all_users(self) -> list[User]:
        return await self.repo.get_all_users()
