from fastapi import APIRouter, Depends
from app.schemas.user import UserResponse, UserCreate
from app.db.session import get_db
from app.services.user_service import UserService
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/users", response_model=UserResponse)
async def create_user(data: UserCreate, session: AsyncSession = Depends(get_db)):
    service = UserService(session)
    return await service.create_user(name=data.name)


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, session: AsyncSession = Depends(get_db)):
    service = UserService(session)
    return await service.get_user_by_id(user_id)


@router.get("/users", response_model=list[UserResponse])
async def get_users(session: AsyncSession = Depends(get_db)):
    service = UserService(session)
    return await service.get_all_users()
