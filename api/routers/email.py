from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from api.dependencies import get_db, get_current_active_user, is_email_verified
from models.api import UserInDB, Subscription
from models.covid_data.school_cases_by_district import SchoolDistricts
from utils.database import verify_email, add_subscription, get_email
from utils.subscriptions import generate_subscription_id

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
async def verify_email_route(
    uuid_str: str, verification_string: str,
    db: Session = Depends(get_db)
):
    verified = verify_email(db, uuid_str, verification_string)
    if verified is False:
        raise HTTPException(status_code=401, detail="Failed to verify email")


@router.put("/subscription")
async def subscribe(
    email_address: str,
    school_district: SchoolDistricts,
    email_verified=Depends(is_email_verified),
    current_user: UserInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    if current_user.email != email_address:
        raise HTTPException(status_code=403, detail="Email address does not match your current email.")

    email = get_email(db, email_address)

    subscription = Subscription(
        id=generate_subscription_id(email.uuid, school_district.name),
        email=email_address,
        district=school_district
    )
    add_subscription(db, subscription)


@router.get("/subscription")
async def subscriptions(
    email_verified: bool = Depends(is_email_verified),
    current_user: UserInDB = Depends(get_current_active_user)
):
    return email_verified
