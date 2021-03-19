import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.exc import IntegrityError
from starlette.requests import Request

from api.routers import auth, subscriptions, users, email

app = FastAPI(
    title="FastAPI example project",
    version="0.1"
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(email.router)
app.include_router(subscriptions.router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# TODO
#   Add password resetting via email

@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    details = "Invalid data"
    if "duplicate key" in str(exc):
        # TODO this could be made more specific. This could also be removed as it leaks information.
        details = "This username or email already exists, please choose another."
    return JSONResponse(
        status_code=403,
        content={"detail": details}
    )


@app.get("/", include_in_schema=False)
def root():
    return {"msg": "root"}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
