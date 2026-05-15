from pydantic import BaseModel


class DeviceCreate(BaseModel):
    user_id: int
    name: str


class DeviceResponse(BaseModel):
    id: int
    user_id: int
    name: str

    class Config:
        from_attributes = True
