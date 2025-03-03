from typing import List

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    password: str
    username: str


class Users(BaseModel):
    users: List[User]


class GetUser(User):
    pass
