from fastapi import HTTPException
from src.transactions_project.schemas.usersSchemas import *
from sqlalchemy.orm import Session
from src.transactions_project.crud.usersCrud import *

def create_user(user: CreateUser, db: Session):
    if user.password == user.submit_password:
        db_user = create(user, db)
        return db_user
    raise HTTPException(status_code=400, detail = "The passwords dont match")

    

