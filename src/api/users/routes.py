from typing import List

from fastapi import APIRouter, Depends

from src.api.users import schemas
from src.api.users.utils import get_users

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=schemas.Users)
async def get_users(users: List[schemas.User] = Depends(get_users)):
    return schemas.Users(users=users)
