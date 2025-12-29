import random
from fastapi import Depends, HTTPException
from src.transactions_project.schemas.usersSchemas import *
from sqlalchemy.orm import Session
from src.transactions_project.crud.usersCrud import *
from src.transactions_project.auth.jwt import create_access_token

def create_user(user: CreateUser, db: Session):
    db_email = findEmail(user.email, db)
    if db_email != None:
        db.rollback()
        raise HTTPException(status_code=409, detail="User with this email is exist")
    if user.password == user.submit_password:
        db_user = create(user, db)
        return db_user
    db.rollback()
    raise HTTPException(status_code=400, detail = "The passwords dont match")

def user_login(email: str, password: str, db: Session):
    db_user = findUser(email, password, db)
    if not db_user:
        db.rollback()
        raise HTTPException(status_code=404, detail="User not found")
    access_token = create_access_token(db_user.id)
    return {"access_token": access_token, "token_type": "bearer"}


def user_delete(user_id: int, db: Session):
    db_user = findUserById(user_id, db)
    if not db_user:
        db.rollback()
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user_id = deleteUser(db_user, db)
    return deleted_user_id

def get_user_by_id(user_id: int, db: Session):
    db_user = findUserById(user_id, db)
    if not db_user:
        db.rollback()
        raise HTTPException(status_code=404, detail="User not found")
    return db_user   

def update_user(user_id: int, user: Login, db: Session):
    same_psw = findSameEmail(user_id, user.email, db)
    if same_psw != None:
        db.rollback()
        raise HTTPException(status_code=409, detail="User with this email is exist")
    updated_db_user = update(user_id, user, db)
    return updated_db_user

def generate_code():
    return str(random.randint(1000, 9999))


