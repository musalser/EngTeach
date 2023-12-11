from sqlalchemy import Boolean, Column, Integer, String, text
from passlib.context import CryptContext
from app.db.base_class import Base


class User(Base):
    __tablename__ = 'users'
    
    username = Column(String, primary_key=True)
    full_name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, server_default="false")
    role = Column(String, server_default=text("'user'"))
