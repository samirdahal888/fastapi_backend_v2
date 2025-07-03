from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import select

from config import ACCESS_TOKEN_EXPIRE_MINUTES
from create_token import create_access_token
from database import SessionDep
from hash_password import get_password_hashed, verify_password
from module import Admin, AdminCreate, AdminPublic
from schema import Token

router = APIRouter(tags=["ADMIN"])


@router.post("/Admin", response_model=AdminPublic)
async def create_admin(request: AdminCreate, session: SessionDep) -> dict:
    db_admin = Admin.model_validate(request)
    db_admin.password = get_password_hashed(db_admin.password)
    session.add(db_admin)
    session.commit()
    session.refresh(db_admin)
    return db_admin


@router.post("/Admin/login")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: SessionDep
) -> Token:
    statement = select(Admin).where(Admin.username == form_data.username)
    user = session.exec(statement=statement).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{form_data.username} username not found ",
        )
    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Incorrect Password"
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
