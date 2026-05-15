from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.stats import Stats


class StatsRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_stats(self, device_id: int, x: float, y: float, z: float) -> Stats:
        stat = Stats(device_id=device_id, x=x, y=y, z=z)
        self.session.add(stat)
        await self.session.commit()
        await self.session.refresh(stat)
        return stat

    async def get_stats(self, device_id: int, from_date: datetime | None = None, to_date: datetime | None = None) -> \
    list[Stats]:
        query = select(Stats).where(Stats.device_id == device_id)

        if from_date:
            query = query.where(Stats.created_at >= from_date)

        if to_date:
            query = query.where(Stats.created_at <= to_date)

        result = await self.session.execute(query)

        return list(result.scalars().all())
