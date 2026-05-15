from pydantic import BaseModel
from datetime import datetime

class StatsCreate(BaseModel):
    device_id: int
    x: float
    y: float
    z: float


class StatsResponse(BaseModel):
    id: int
    device_id: int
    x: float
    y: float
    z: float
    created_at: datetime

    class Config:
        from_attributes = True
