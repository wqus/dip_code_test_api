from fastapi import APIRouter, Depends
from app.schemas.device import DeviceResponse, DeviceCreate
from app.db.session import get_db
from app.services.device_service import DeviceService
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/devices", response_model=DeviceResponse)
async def create_device(data: DeviceCreate, session: AsyncSession = Depends(get_db)):
    service = DeviceService(session)
    return await service.create_device(data.user_id, data.name)

@router.get("/devices/{device_id}", response_model=DeviceResponse)
async def get_device(device_id: int, session: AsyncSession = Depends(get_db)):
    service = DeviceService(session)
    return await service.get_device_by_id(device_id)

@router.get("/devices/user/{user_id}", response_model=list[DeviceResponse])
async def get_devices_by_user(user_id: int, session: AsyncSession = Depends(get_db)):
    service = DeviceService(session)
    return await service.get_devices_by_user_id(user_id)