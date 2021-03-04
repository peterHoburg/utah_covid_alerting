from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.dependencies import get_db
from models.api import APIToken
from utils.auth import authenticate_user, create_access_token

router = APIRouter(
    # prefix="/auth",
    tags=["auth"],
)


@router.post("/token", response_model=APIToken)
async def get_token_with_password(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(user)
    return {"access_token": access_token, "token_type": "bearer"}
