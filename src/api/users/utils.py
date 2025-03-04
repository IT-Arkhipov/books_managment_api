from typing import List

from fastapi import Depends

from src.api.users import schemas
from src.api.users.auth import is_admin
from src.data.users_db import users


def get_users() -> List[schemas.User]:
    return [schemas.GetUser(**user) for user in users]


def create_user(new_user: schemas.User, is_admin_role=Depends(is_admin)):
    for user in users:
        if user.get('email') == new_user.email:
            users.remove(user)
    users.append(new_user.model_dump())
    return new_user
