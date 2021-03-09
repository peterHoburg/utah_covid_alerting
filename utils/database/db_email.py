from sqlalchemy.orm import Session

from models import sql
from models.api import Email


def verify_(db: Session, uuid_str: str, verification_string: str) -> bool:
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


def get_(db: Session, email: str) -> Email:
    return Email.from_orm(db.query(sql.Email).filter(sql.Email.address == email).first())
