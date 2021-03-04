from fastapi import Depends, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.dependencies import get_db
from src.utils.database import verify_email

router = APIRouter(
    prefix="/email",
    tags=["email"]
)


@router.put(
    "/verify/",
    responses={
        200: {"description": "Verified email address"},
        401: {"description": "Failed to verify email"},
    }
)
async def read_users_me(uuid_str: str, verification_string: str, db: Session = Depends(get_db)):
    verified = verify_email(db, uuid_str, verification_string)
    if verified is False:
        raise HTTPException(status_code=401, detail="Failed to verify email")
