from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class APIToken(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    iss: str = "TestApp"
    sub: str
    exp: datetime
    nbf: datetime
    iat: datetime
    name: str
    email: str


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    enabled: Optional[bool] = None

    class Config:
        orm_mode = True


class UserInDB(User):
    password: str
