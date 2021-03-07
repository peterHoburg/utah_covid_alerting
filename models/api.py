from datetime import datetime
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, validator
from validate_email import validate_email

from models.covid_data.school_cases_by_district import SchoolDistricts


def _email_validate(email_string):
    is_valid = validate_email(
        email_address=email_string,
        check_regex=True,
        check_mx=False,
        use_blacklist=False,
        skip_smtp=True
    )
    if is_valid is False:
        raise HTTPException(
            status_code=422,
            detail="Invalid Email Address"
        )
    return email_string


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

    @validator("email")
    def email_validate(cls, email_string: str):
        return _email_validate(email_string)

    class Config:
        orm_mode = True


class UserInDB(User):
    password: str


class Email(BaseModel):
    address: str
    uuid: str
    verified: bool = False
    verification_string: str

    class Config:
        orm_mode = True


class Subscription(BaseModel):
    """
    Used for subscriptions when the data is being passed to the user.
    """
    email: str
    district: SchoolDistricts

    @validator("email")
    def email_validate(cls, email_string: str):
        return _email_validate(email_string)

    class Config:
        orm_mode = True


class SubscriptionDB(Subscription):
    id: str
