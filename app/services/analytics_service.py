from datetime import datetime
from statistics import median

from sqlalchemy.ext.asyncio import AsyncSession

from app.services.device_service import DeviceService
from app.services.stats_service import StatsService


class AnalyticsService:

    def __init__(self, session: AsyncSession):
        self.stats_service = StatsService(session)
        self.device_service = DeviceService(session)

    @staticmethod
    def calculate_metrics(values: list[float]) -> dict:
        if not values:
            return {
                "min": None,
                "max": None,
                "sum": 0,
                "count": 0,
                "median": None,
            }

        return {
            "min": min(values),
            "max": max(values),
            "sum": sum(values),
            "count": len(values),
            "median": median(values),
        }

    async def get_device_analysis(self, device_id: int, from_date: datetime | None = None,
                                  to_date: datetime | None = None) -> dict:
        stats = await self.stats_service.get_stats(
            device_id=device_id,
            from_date=from_date,
            to_date=to_date,
        )

        if not stats:
            return {
                "x": self.calculate_metrics([]),
                "y": self.calculate_metrics([]),
                "z": self.calculate_metrics([]),
            }

        return {
            "x": self.calculate_metrics([stat.x for stat in stats]),
            "y": self.calculate_metrics([stat.y for stat in stats]),
            "z": self.calculate_metrics([stat.z for stat in stats]),
        }

    async def get_user_analysis(self, user_id: int, from_date: datetime | None = None,
                                to_date: datetime | None = None) -> dict:
        devices = await self.device_service.get_devices_by_user_id(user_id)

        all_stats = []
        for device in devices:
            stats = await self.stats_service.get_stats(
                device_id=device.id,
                from_date=from_date,
                to_date=to_date,
            )
            all_stats.extend(stats)

        if not all_stats:
            return {
                "x": self.calculate_metrics([]),
                "y": self.calculate_metrics([]),
                "z": self.calculate_metrics([]),
            }

        return {
            "x": self.calculate_metrics([s.x for s in all_stats]),
            "y": self.calculate_metrics([s.y for s in all_stats]),
            "z": self.calculate_metrics([s.z for s in all_stats]),
        }

    async def get_user_devices_analysis(self, user_id: int, from_date: datetime | None = None,
                                        to_date: datetime | None = None) -> dict:
        devices = await self.device_service.get_devices_by_user_id(user_id)

        result = {}

        for device in devices:
            result[f"device_{device.id}"] = await self.get_device_analysis(
                device_id=device.id,
                from_date=from_date,
                to_date=to_date,
            )

        return {"devices": result}
