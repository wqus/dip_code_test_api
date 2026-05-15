from pydantic import BaseModel

class Metrics(BaseModel):
    min: float | None
    max: float | None
    sum: float
    count: int
    median: float | None

class DeviceAnalyticsResponse(BaseModel):
    x: Metrics
    y: Metrics
    z: Metrics

class UserDeviceAnalyticsResponse(BaseModel):
    devices: dict[str, DeviceAnalyticsResponse]