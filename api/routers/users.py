from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from api.dependencies import get_db
from api.models.api import UserInDB
from utils.database import put_user

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.post("", status_code=201)
async def new_(new_user: UserInDB, db: Session = Depends(get_db)):
    put_user(db, new_user)
