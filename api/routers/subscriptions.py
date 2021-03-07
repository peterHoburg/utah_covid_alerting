from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from api.dependencies import get_db, get_current_active_user, is_email_verified
from models.api import UserInDB, SubscriptionDB
from models.covid_data.school_cases_by_district import SchoolDistricts
from utils.database import add_subscription, get_email, get_subscriptions, delete_subscriptions
from utils.subscriptions import generate_subscription_id

router = APIRouter(
    prefix="/subscriptions",
    tags=["Subscriptions"]
)


@router.get("/subscription")
async def subscriptions(
    email_verified: bool = Depends(is_email_verified),
    current_user: UserInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    return get_subscriptions(db, current_user.email)


@router.post("/subscription")
async def subscribe(
    school_district: SchoolDistricts,
    email_verified=Depends(is_email_verified),
    current_user: UserInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    email = get_email(db, current_user.email)

    subscription = SubscriptionDB(
        id=generate_subscription_id(email.uuid, school_district.name),
        email=current_user.email,
        district=school_district
    )
    add_subscription(db, subscription)


@router.delete("/subscription")
async def delete_subscriptions_route(
    districts_to_remove: list[SchoolDistricts],
    email_verified: bool = Depends(is_email_verified),
    current_user: UserInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    delete_subscriptions(db, current_user.email, districts_to_remove)
