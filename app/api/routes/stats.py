from fastapi import APIRouter, Depends
from app.schemas.stats import StatsCreate, StatsResponse
from app.db.session import get_db
from app.services.stats_service import StatsService
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

router = APIRouter()


@router.post("/stats", response_model=StatsResponse)
async def create_stats(data: StatsCreate, session: AsyncSession = Depends(get_db)):
    service = StatsService(session)
    return await service.create_stat(data.device_id, data.x, data.y, data.z)


@router.get("/stats/{device_id}", response_model=list[StatsResponse])
async def get_stats(device_id: int, from_date: datetime | None = None, to_date: datetime | None = None,
                    session: AsyncSession = Depends(get_db)):
    service = StatsService(session)
    return await service.get_stats(device_id, from_date, to_date)
