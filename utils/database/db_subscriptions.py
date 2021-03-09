from sqlalchemy.orm import Session

from models import sql
from models.api import SubscriptionDB, Subscription
from models.covid_data.school_cases_by_district import SchoolDistricts


def add_(db: Session, subscription: SubscriptionDB):
    sub_dict = subscription.dict()
    sub_dict["district"] = subscription.district.value
    subscription = sql.Subscription(**sub_dict)
    try:
        db.add(subscription)
    except Exception:
        db.rollback()
        raise
    finally:
        db.commit()


def get_(db: Session, email: str) -> list[Subscription]:
    subs = db.query(sql.Subscription).filter(sql.Subscription.email == email).all()
    for sub in subs:
        print(sub.email)
        Subscription.from_orm(sub)
    return [Subscription.from_orm(sub) for sub in subs]


def delete_(db: Session, email: str, districts: list[SchoolDistricts]):
    try:
        for district in districts:
            db.query(sql.Subscription).filter(
                sql.Subscription.email == email and sql.Subscription.district == district.value
            ).delete()
    except Exception:
        db.rollback()
        raise
    finally:
        db.commit()
