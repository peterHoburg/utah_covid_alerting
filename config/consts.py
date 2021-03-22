import os
import re

import boto3
from botocore.config import Config
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# openssl rand -hex 32
SECRET_KEY = os.environ.get("SECRET_KEY_ENV", "1e752489cd7e8603c9baf984849cf3750791aa675c5c728041782b470674ec33")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

POSTGRES_DATABASE_URL = os.environ.get("POSTGRES_DATABASE_URL_ENV", "postgresql://test:test@postgres/test")

engine = create_engine(POSTGRES_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

UTAH_COVID19_DOWNLOAD_URL = "https://coronavirus-dashboard.utah.gov/Utah_COVID19_data.zip"

YYYY_MM_DD_REGEX = re.compile("2[0-9]{3}-[0-9]{2}-[0-9]{2}")

S3_CLIENT = boto3.client('s3', config=Config(signature_version='s3v4'), endpoint_url=os.environ.get('S3_ENDPOINT_URL'))
S3_DATA_BUCKET = "utah-data"
