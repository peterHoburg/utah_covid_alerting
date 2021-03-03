from sqlalchemy.orm import Session

from src.models import sql
from src.models.api import UserInDB


def get_user(db: Session, username: str) -> UserInDB:
    return UserInDB.from_orm(db.query(sql.User).filter(sql.User.username == username).first())


