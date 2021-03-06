from sqlalchemy import Boolean, Column, String, ForeignKey

from config.consts import Base


class Email(Base):
    __tablename__ = "email"
    address = Column(String, primary_key=True, index=True)
    uuid = Column(String, index=True)
    verified = Column(Boolean, default=False)
    verification_string = Column(String, nullable=False)


class User(Base):
    __tablename__ = "user"
    username = Column(String, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, ForeignKey(Email.address))
    password = Column(String)
    enabled = Column(Boolean)


class Subscription(Base):
    __tablename__ = "subscription"
    id = Column(String, primary_key=True, index=True)
    email = Column(String, ForeignKey(Email.address), index=True)
    district = Column(String, nullable=False)
