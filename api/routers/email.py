from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from api.dependencies import get_db
from models.covid_data.school_cases_by_district import SchoolDistricts
from utils.database import verify_email

router = APIRouter(
    prefix="/email",
    tags=["email"]
)


@router.put(
    "/verify/",
    responses={
        200: {"description": "Verified email address"},
        401: {"description": "Failed to verify email"},
    }
)
async def verify_email(uuid_str: str, verification_string: str, db: Session = Depends(get_db)):
    verified = verify_email(db, uuid_str, verification_string)
    if verified is False:
        raise HTTPException(status_code=401, detail="Failed to verify email")


@router.put("/subscription")
async def subscribe(email_address: str, school_district: SchoolDistricts):
    pass


@router.get("/subscription")
async def subscriptions(email_address: str):
    pass
