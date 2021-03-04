import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.exc import IntegrityError
from starlette.requests import Request

from src.routers import auth
from src.routers import users

app = FastAPI(
    title="FastAPI example project",
    version="0.1"
)

app.include_router(auth.router)
app.include_router(users.router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    details = "Invalid data"
    if "duplicate key" in str(exc):
        # TODO this could be made more specific. This could also be removed as it leaks information.
        details = "This username or email already exists, please choose another."
    return JSONResponse(
        status_code=501,
        content={"detail": details}
    )


@app.get("/", include_in_schema=False)
def root():
    return {"hello": "world"}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
