from sqlalchemy.ext.asyncio import AsyncSession
from app.models.stats import Stats
from app.repositories.stats_repo import StatsRepository
from datetime import datetime

class StatsService:
    def __init__(self, session: AsyncSession):
        self.repo = StatsRepository(session)

    async def create_stat(self, device_id: int, x: float, y: float, z: float) -> Stats:
        return await self.repo.create_stats(device_id, x, y, z)

    async def get_stats(self, device_id: int, from_date: datetime | None = None, to_date: datetime | None = None) ->  list[Stats]:
        return await self.repo.get_stats(device_id, from_date, to_date)
