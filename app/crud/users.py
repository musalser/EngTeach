
from typing import Any, Dict, Union
from passlib.hash import bcrypt
from app import models
from app import schemes
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from app.crud.base import CRUDBase

class CRUDDocument(CRUDBase[models.User, schemes.UserCreate, schemes.UserUpdate]):

    def create(self, db: Session, *, obj_in: schemes.UserCreate) -> models.User:
        obj_in_data = jsonable_encoder(obj_in)
        password = obj_in_data.pop("password")
        obj_in_data["hashed_password"] = bcrypt.hash(password)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: models.User,
        obj_in: Union[schemes.UserUpdate, Dict[str, Any]]
    ) -> models.User:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        if "password" in update_data:
            update_data["hashed_password"] = bcrypt.hash(update_data["password"])
            del update_data["password"]
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
user = CRUDDocument(models.User)