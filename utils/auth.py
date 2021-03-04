from datetime import datetime, timedelta
from typing import Union

from jose import jwt
from sqlalchemy.orm import Session

from config.consts import pwd_context, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from api.models.api import UserInDB, TokenPayload
from utils import get_user

__all__ = ["authenticate_user", "create_access_token", "username_from_jwt_subject"]


def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not _verify_password(password, user.password):
        return False
    return user


def create_access_token(user: UserInDB, expires_in_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    expire = datetime.utcnow() + timedelta(minutes=expires_in_minutes)

    token_payload = TokenPayload(
        sub=generate_jwt_subject(user.username),
        exp=expire,
        nbf=datetime.utcnow(),
        iat=datetime.utcnow(),
        name=user.full_name,
        email=user.email
    )

    encoded_jwt = jwt.encode(token_payload.dict(), SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def username_from_jwt_subject(token_subject: str) -> Union[str, None]:
    try:
        username = token_subject.split("username:")[1]
        return username
    except Exception:
        return None


def generate_jwt_subject(username: str) -> str:
    subject = f"username:{username}"
    return subject


def _verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def _get_password_hash(password):
    return pwd_context.hash(password)
