from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette import status

from src.api.users import schemas
from src.data.users_db import users

security = HTTPBasic()


def authenticate(authenticated_user: HTTPBasicCredentials = Depends(security)) -> schemas.User:
    for user in users:
        if authenticated_user.username == user.get('email') or authenticated_user.password == user.get('password'):
            return schemas.User(**user)

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized",
                        headers={"WWW-Authenticate": "Basic"},)


def is_admin(user=Depends(authenticate)):
    if user.role != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Forbidden: Authorized user does not have the required admin role."
                            )
    return True
