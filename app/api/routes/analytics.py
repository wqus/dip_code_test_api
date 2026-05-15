from fastapi import APIRouter, Depends
from app.schemas.analytics import UserDeviceAnalyticsResponse, Metrics, DeviceAnalyticsResponse
from app.db.session import get_db
from app.services.analytics_service import AnalyticsService
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

router = APIRouter()


@router.get("/analytics/device/{device_id}", response_model=DeviceAnalyticsResponse)
async def device_analysis(device_id: int, from_date: datetime | None = None, to_date: datetime | None = None,
                          session: AsyncSession = Depends(get_db)):
    service = AnalyticsService(session)
    return await service.get_device_analysis(device_id, from_date, to_date)


@router.get("/analytics/user/{user_id}", response_model=DeviceAnalyticsResponse)
async def user_analysis(user_id: int, from_date: datetime | None = None, to_date: datetime | None = None,
                        session: AsyncSession = Depends(get_db)):
    service = AnalyticsService(session)
    return await service.get_user_analysis(user_id, from_date, to_date)


@router.get("/analytics/user/{user_id}/devices", response_model=UserDeviceAnalyticsResponse)
async def user_devices_analysis(user_id: int, from_date: datetime | None = None, to_date: datetime | None = None,
                                session: AsyncSession = Depends(get_db)):
    service = AnalyticsService(session)
    return await service.get_user_devices_analysis(user_id, from_date, to_date)
