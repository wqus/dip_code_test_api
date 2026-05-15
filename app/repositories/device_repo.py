from app.models import Device
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class DeviceRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_device(self, user_id: int, name: str) -> Device:
        device = Device(user_id=user_id, name=name)
        self.session.add(device)

        await self.session.commit()
        await self.session.refresh(device)

        return device

    async def get_device_by_id(self, device_id: int) -> Device | None:
        result = await self.session.execute(select(Device).where(Device.id == device_id))
        return result.scalar_one_or_none()

    async def get_devices_by_user_id(self, user_id: int) -> list[Device]:
        result = await self.session.execute(select(Device).where(Device.user_id == user_id))
        return list(result.scalars().all())

    async def get_all_devices(self) -> list[Device]:
        result = await self.session.execute(select(Device))
        return list(result.scalars().all())
