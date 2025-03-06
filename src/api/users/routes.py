from typing import List

from fastapi import APIRouter, Depends

from src.api.users import schemas
from src.api.users.auth import authenticate
from src.api.users.utils import get_users, create_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=schemas.Users)
async def get_users(users: List[schemas.GetUser] = Depends(get_users)):
    return schemas.Users(users=users)


@router.put("/", response_model=schemas.User, summary="Create user")
async def create_user(
    new_user: schemas.User = Depends(create_user), user=Depends(authenticate)
):
    """
    Creating user. Only user with admin role can create new user.
    Authorization: default user with admin role: email=test@test.com, password=test_test
    """
    return new_user
