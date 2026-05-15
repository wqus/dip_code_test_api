from sqlalchemy.ext.asyncio import AsyncSession
from app.models.device import Device
from app.repositories.device_repo import DeviceRepository


class DeviceService:
    def __init__(self, session: AsyncSession):
        self.repo = DeviceRepository(session)

    async def create_device(self, user_id: int, name: str) -> Device:
        return await self.repo.create_device(user_id, name)

    async def get_device_by_id(self, device_id: int) -> Device | None:
        return await self.repo.get_device_by_id(device_id)

    async def get_devices_by_user_id(self, user_id: int) -> list[Device]:
        return await self.repo.get_devices_by_user_id(user_id)

    async def get_all_devices(self) -> list[Device]:
        return await self.repo.get_all_devices()
