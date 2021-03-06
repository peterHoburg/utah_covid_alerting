import hashlib
import uuid

from sqlalchemy.orm import Session

from models import sql
from models.api import UserInDB, Email, Subscription


def get_user(db: Session, username: str) -> UserInDB:
    return UserInDB.from_orm(db.query(sql.User).filter(sql.User.username == username).first())


def put_user(db: Session, user: UserInDB):
    uuid_str = str(uuid.uuid4())
    sha256 = hashlib.sha256()
    sha256.update(user.email.encode("UTF-8"))
    sha256.update(uuid_str.encode("UTF-8"))
    # TODO using a random UUID4 and the users email to generate the sha256 hash means if someone figures out the
    #   uuid they could replicate the verification code. Is this bad? Would anyone know the UUID outside of the
    #   person who get the email link? In that case does it matter? This also means only one verification_string
    #   can be generated...

    hex_digest = sha256.hexdigest()
    email = Email(
        address=user.email,
        uuid=uuid_str,
        verified=False,
        verification_string=hex_digest
    )
    email = sql.Email(**email.dict())
    user = sql.User(**user.dict())
    try:
        db.add(email)
        db.commit()
        db.add(user)
    except Exception:
        db.rollback()
        raise
    finally:
        db.commit()


def verify_email(db: Session, uuid_str: str, verification_string: str) -> bool:
    try:
        data = db.query(sql.Email).filter(sql.Email.uuid == uuid_str).first()

        if data is not None and verification_string == data.verification_string:
            data.verified = True
            db.commit()
            return True
        return False
    except Exception:
        db.rollback()
        raise


def get_email(db: Session, email: str) -> Email:
    return Email.from_orm(db.query(sql.Email).filter(sql.Email.address == email).first())


def add_subscription(db: Session, subscription: Subscription):
    sub_dict = subscription.dict()
    sub_dict["district"] = subscription.district.name
    subscription = sql.Subscription(**sub_dict)
    try:
        db.add(subscription)
    except Exception:
        db.rollback()
        raise
    finally:
        db.commit()
