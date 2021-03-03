import hashlib
import uuid

from sqlalchemy.orm import Session

from src.models import sql
from src.models.api import UserInDB, Email


def get_user(db: Session, username: str) -> UserInDB:
    return UserInDB.from_orm(db.query(sql.User).filter(sql.User.username == username).first())


def put_user(db: Session, user: UserInDB):
    uuid_str = str(uuid.uuid4())
    sha256 = hashlib.sha256()
    sha256.update(user.email.encode("UTF-8"))
    sha256.update(uuid_str.encode("UTF-8"))
    hex_digest = sha256.hexdigest()
    email = Email(
        address=user.email,
        uuid=uuid_str,
        verified=False,
        verification_string=hex_digest
    )
    email = sql.Email(**email.dict())
    user = sql.User(**user.dict())
    db.add(email)
    db.commit()
    db.add(user)
    db.commit()
