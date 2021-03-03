from sqlalchemy import Boolean, Column, String

from src.conf.config import Base


class User(Base):
    __tablename__ = "user"
    username = Column(String, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String)
    password = Column(String)
    enabled = Column(Boolean)
