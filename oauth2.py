from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from sqlmodel import select

from config import ALGORITHM, SECRET_KEY
from database import SessionDep
from module import Admin
from schema import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="Admin/login")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)], session: SessionDep
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    statement = select(Admin).where(Admin.username == username)
    user = session.exec(statement=statement).first()
    if user is None:
        raise credentials_exception
    return user
