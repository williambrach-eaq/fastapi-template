from abc import ABC
from typing import Dict

from application.main.config import settings
from application.main.infrastructure.database.db_interface import DataBaseOperations
from application.main.utility.config_loader import ConfigReaderInstance


from sqlalchemy.orm import Session
from application.main.infrastructure.database.db_postgresql import SessionLocal
from . import models, schemas

class PostgresDb():
    def update_single_db_record(email: str):
        db = SessionLocal()
        item = (
            db.query(models.User)
            .filter.filter(models.User.email == email)
            .first()
            .update({"email": "kekw2"})
        )
        db.commit()
        db.close()
        return item


    def update_multiple_db_record(email: str):
        db = SessionLocal()
        item = (
            db.query(models.User)
            .filter.filter(models.User.email == email)
            .update({"email": "kekw2"})
        )
        db.commit()
        db.close()
        return item


    def fetch_single_db_record(email: str):
        db = SessionLocal()
        item = db.query(models.User).filter(models.User.email == email).first()
        db.close()
        return item


    def fetch_multiple_db_record(skip: int = 0, limit: int = 100):
        db = SessionLocal()
        items = db.query(models.User).offset(skip).limit(limit).all()
        print(items)
        db.close()
        return items


    def insert_single_db_record(user: schemas.UserCreate):
        db = SessionLocal()
        db_user = models.User(email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        db.close()
        return db_user


    def insert_multiple_db_record():
        db = SessionLocal()
        
        objects = [models.User(id=10,email="u1"), models.User(id=11,email="u2"), models.User(id=12,email="u3")]
        db.bulk_save_objects(objects)
        db.commit()
        db.close()


    def delete_single_db_record():
        db = SessionLocal()
        user = db.query(models.User).filter(models.User.email == 1).first()
        db.delete(user)
        db.commit()
        db.close()


    def delete_multiple_db_record():
        db = SessionLocal()
        db.query(models.User).filter(models.User.email.in_(["kek"])).delete(
            synchronize_session=False
        )
        db.commit()
        db.close()
