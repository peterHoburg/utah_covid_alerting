from datetime import datetime
from enum import Enum
from typing import Optional

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from src.dependencies import get_current_active_user
from src.models.api import User
from src.routers import auth
from src.routers import users

app = FastAPI(
    title="FastAPI example project",
    version="0.1"
)

app.include_router(auth.router)
app.include_router(users.router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class TestEnum(Enum):
    test_val1 = "test1"
    test_val2 = "test2"


class BodyExample(BaseModel):
    name: str
    age: int
    date: Optional[datetime]


@app.get("/", include_in_schema=False)
def root():
    return {"hello": "world"}


@app.get("/enum_test/{enum_val}")
def test_enum(enum_val: TestEnum, user: User = Depends(get_current_active_user)):
    return {"value": enum_val}


@app.get("/query_example/")
async def query_example(query_option_1: TestEnum, query_option_2: bool = False, query_option_3: Optional[str] = None,
                        token: str = Depends(oauth2_scheme)):
    return {"done": "done"}


@app.post("/body_example/")
async def body_example(example: BodyExample):
    pass


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
