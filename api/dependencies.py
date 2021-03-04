from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from config.consts import oauth2_scheme, SECRET_KEY, ALGORITHM, SessionLocal
from models.api import UserInDB
from utils.auth import username_from_jwt_subject
from utils.database import get_user


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> UserInDB:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        token_subject: str = payload.get("sub")
        username = username_from_jwt_subject(token_subject)
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user(db, username)
    if user is None:
        raise credentials_exception

    return user


async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if current_user.enabled is False:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
