from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from app.schemes.user import UserInDB, User
from app.core.jwt import verify_token
from fastapi import Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.users import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(username: str|None, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    return user

def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
    user = get_user(username, db)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def get_current_user_role(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    data = verify_token(token)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return data.get("role")

def get_token_data(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    data = verify_token(token)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return data



class PermissionChecker:

    def __init__(self, required_permissions: list[str]|None = None) -> None:
        if not required_permissions:
            self.required_permissions = ["user"]
        else:
            self.required_permissions = required_permissions

    def __call__(self, token_data: str = Depends(get_token_data)) -> bool:
        role = token_data.get("role")
        if role not in self.required_permissions:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not enough permissions",
            headers={"WWW-Authenticate": "Bearer"},
        )
        return token_data