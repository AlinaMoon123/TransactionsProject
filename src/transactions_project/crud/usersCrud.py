from datetime import timezone
from sqlalchemy import select
from src.transactions_project.schemas.usersSchemas import *
from sqlalchemy.ext.asyncio import AsyncSession
from src.transactions_project.models.users import Users
from src.transactions_project.models import users

async def create(user: CreateUser, db: AsyncSession):
    db_user = Users(name=user.name, password=user.password, email=user.email)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

    
async def findUser(email: str, password: str, db: AsyncSession):
    stmt=select(Users).where(Users.email==email, Users.password==password)
    res=await db.execute(stmt)
    return res.scalars().first()

async def deleteUser(user: Users, db: AsyncSession):
    user_id=user.id
    await db.delete(user)
    await db.commit()
    return user_id

async def findUserById(user_id: int, db: AsyncSession):
    stmt=select(Users).where(Users.id==user_id)
    res=await db.execute(stmt)
    return res.scalars().first()

async def findSameEmail(user_id: int, email: str, db: AsyncSession):
    stmt=select(Users).where(Users.id!=user_id, Users.email==email)
    res=await db.execute(stmt)
    return res.scalars().first()

async def findEmail(email: str, db: AsyncSession):
    stmt=select(Users).where(Users.email==email)
    res=await db.execute(stmt)
    return res.scalars().first()

async def update(user_id: int, user: UpdateUser, db: AsyncSession):
    db_user = await findUserById(user_id, db)
    if user.email != None:
        db_user.email = user.email
    if user.name != None:
        db_user.name = user.name
    if user.password != None:
        db_user.password = user.password
    update_time = datetime.now(timezone.utc)
    if user.email == None and user.name == None and user.password == None:
        update_time = db_user.update_at
    db_user.update_at = update_time
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def activateUser(email: int, db: AsyncSession):
    db_user = await findEmail(email, db)
    db_user.is_active = True
    await db.commit()
    return db_user