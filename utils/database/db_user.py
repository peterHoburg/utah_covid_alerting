import hashlib
import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import sql
from models.api import UserInDB, Email


def get_(db: Session, username: str) -> UserInDB:
    user = db.query(sql.User).filter(sql.User.username == username).first()
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid User"
        )
    return UserInDB.from_orm(user)


# noinspection InsecureHash
def put_(db: Session, user: UserInDB):
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


def delete_(db: Session, user: UserInDB):
    try:
        db.query(sql.User).filter(sql.User.email == user.email).delete()
        db.query(sql.Subscription).filter(sql.Subscription.email == user.email).delete()
        db.query(sql.Email).filter(sql.Email.address == user.email).delete()
    except Exception:
        db.rollback()
        raise
    finally:
        db.commit()


def update_status(db: Session, user: UserInDB, status: bool):
    try:
        data = db.query(sql.User).filter(sql.User.email == user.email).first()
        data.enabled = status
    except Exception:
        db.rollback()
        raise
    finally:
        db.commit()
