import random
from fastapi import HTTPException
from sqlalchemy import update
from src.transactions_project.schemas.usersSchemas import CreateUser, Login  
from sqlalchemy.ext.asyncio import AsyncSession
from src.transactions_project.crud.usersCrud import create, deleteUser, findEmail, findSameEmail, findUser, findUserById 
from src.transactions_project.auth.jwt import create_access_token

async def create_user(user: CreateUser, db: AsyncSession):
    db_email = await findEmail(user.email, db)
    if db_email:
        raise HTTPException(status_code=409, detail="User with this email is exist")
    if user.password == user.submit_password:
        db_user = await create(user, db)
        return db_user
    raise HTTPException(status_code=400, detail = "The passwords dont match")

async def user_login(email: str, password: str, db: AsyncSession):
    db_user = await findUser(email, password, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    access_token=create_access_token(db_user.id)
    return {"access_token": access_token, "token_type": "bearer"}


async def user_delete(user_id: int, db: AsyncSession):
    db_user = await findUserById(user_id, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user_id = await deleteUser(db_user, db)
    return deleted_user_id

async def get_user_by_id(user_id: int, db: AsyncSession):
    db_user = await findUserById(user_id, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user   

async def update_user(user_id: int, user: Login, db: AsyncSession):
    same_psw = await findSameEmail(user_id, user.email, db)
    if same_psw:
        raise HTTPException(status_code=409, detail="User with this email is exist")
    updated_db_user = await update(user_id, user, db)
    return updated_db_user

def generate_code():
    return str(random.randint(1000, 9999))


