from typing import List

from src.api.users import schemas
from src.data.users_db import users


def get_users() -> List[schemas.User]:
    return [schemas.User(**user) for user in users]
