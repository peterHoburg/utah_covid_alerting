from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from src.dependencies import get_current_active_user, get_db
from src.utils.database import put_user
from src.models.api import User, UserInDB

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/new")
async def new_(new_user: UserInDB, db: Session = Depends(get_db)):
    put_user(db, new_user)



@router.get("/me/items")
async def read_own_items(current_user: UserInDB = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
