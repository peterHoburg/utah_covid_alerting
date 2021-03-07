from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from api.dependencies import get_db
from models.api import UserInDB
from utils.auth import generate_password_hash
from utils.database import db_user

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.post("", status_code=201)
async def new_(new_user: UserInDB, db: Session = Depends(get_db)):
    hashed_password = generate_password_hash(new_user.password)
    new_user.password = hashed_password

    db_user.put_(db, new_user)
