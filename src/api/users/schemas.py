from typing import List, Literal

from pydantic import BaseModel, EmailStr


user_role = Literal["admin", "user"]


class User(BaseModel):
    email: EmailStr
    password: str
    role: user_role


class Users(BaseModel):
    users: List[User]


class GetUser(User):
    pass
