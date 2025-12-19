from src.transactions_project.schemas.usersSchemas import *
from sqlalchemy.orm import Session
from src.transactions_project.models.users import Users

def create(user: CreateUser, db: Session):
    db_user = Users(name = user.name, password = user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

    

