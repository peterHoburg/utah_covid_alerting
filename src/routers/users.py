from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from src.dependencies import get_current_active_user, get_db
from src.models.api import UserInDB
from src.utils.database import put_user

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.post("", status_code=201)
async def new_(new_user: UserInDB, db: Session = Depends(get_db)):
    put_user(db, new_user)
