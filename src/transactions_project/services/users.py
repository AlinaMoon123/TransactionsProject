from fastapi import HTTPException
from src.transactions_project.schemas.usersSchemas import *
from sqlalchemy.orm import Session
from src.transactions_project.crud.usersCrud import *

def create_user(user: CreateUser, db: Session):
    if user.password == user.submit_password:
        db_user = create(user, db)
        return db_user
    raise HTTPException(status_code=400, detail = "The passwords dont match")

def user_login(user: Login, db: Session):
    db_user = findUser(user.name, user.password, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


def user_delete(user_id: int, db: Session):
    db_user = findUserById(user_id, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user_id = deleteUser(db_user, db)
    return deleted_user_id

def get_user_by_id(user_id: int, db: Session):
    db_user = findUserById(user_id, db)
    return db_user   

def update_user(user_id: int, user: Login, db: Session):
    updated_db_user = update(user_id, user, db)
    return updated_db_user

