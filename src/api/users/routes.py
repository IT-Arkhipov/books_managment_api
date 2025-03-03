from typing import List

from fastapi import APIRouter, Depends

from src.api.users import schemas
from src.api.users.utils import get_users, create_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=schemas.Users)
async def get_users(users: List[schemas.GetUser] = Depends(get_users)):
    return schemas.Users(users=users)


@router.put("/", response_model=schemas.User)
async def create_user(user: schemas.User = Depends(create_user)):
    return user
