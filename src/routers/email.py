from fastapi import Depends, APIRouter

from src.dependencies import get_current_active_user
from src.models.api import User, UserInDB

router = APIRouter(
    prefix="/email",
    tags=["email"]
)


@router.post("/verify", response_model=User)
async def read_users_me(current_user: UserInDB = Depends(get_current_active_user)):
    return User(**current_user.dict())


