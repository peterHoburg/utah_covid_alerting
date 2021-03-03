from fastapi import Depends, APIRouter

from src.dependencies import get_current_active_user
from src.models.api import User, UserInDB

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/me", response_model=User)
async def read_users_me(current_user: UserInDB = Depends(get_current_active_user)):
    return User(**current_user.dict())


@router.get("/me/items")
async def read_own_items(current_user: UserInDB = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
