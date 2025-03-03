from typing import List

from src.api.users import schemas
from src.data.users_db import users


def get_users() -> List[schemas.User]:
    return [schemas.GetUser(**user) for user in users]


def create_user(user: schemas.User):
    users.append(user.model_dump())
    return user
