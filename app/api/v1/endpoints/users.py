from typing import List
from fastapi import APIRouter
from fastapi import Depends
from app import models
from app import schemes
from app.services.authentication import PermissionChecker
from app.api.deps import get_db
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import crud

router = APIRouter()

@router.get("/", response_model=List[schemes.User])
def read_users(db: Session = Depends(get_db), token_data: str = Depends(PermissionChecker(["admin"]))):
    return db.query(models.User).all()


@router.post("/register", response_model=schemes.User)

def register(user_in: schemes.UserCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == user_in.username).first()
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")
    user = crud.user.create(db, obj_in=user_in)
    return user

@router.put("/{username}", response_model=schemes.User)
def update_user(username: str, user_in: schemes.UserUpdate, db: Session = Depends(get_db), token_data: str = Depends(PermissionChecker(["user", "admin"]))):
    if token_data.get("username") != username and token_data.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user