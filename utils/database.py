import hashlib
import uuid

from sqlalchemy.orm import Session

from api.models import sql
from api.models.api import UserInDB, Email


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
