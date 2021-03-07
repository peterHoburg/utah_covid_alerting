from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from api.dependencies import get_db, get_current_active_user
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


@router.put("/status", status_code=200)
async def status(
    desired_status: bool,
    current_user: UserInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    db_user.update_status(db, current_user, desired_status)


@router.delete("", status_code=200)
async def delete_(
    current_user: UserInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    db_user.delete_(db, current_user)
