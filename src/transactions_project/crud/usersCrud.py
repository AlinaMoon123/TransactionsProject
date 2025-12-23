from datetime import timezone
from src.transactions_project.schemas.usersSchemas import *
from sqlalchemy.orm import Session
from src.transactions_project.models.users import Users
from src.transactions_project.models import users

def create(user: CreateUser, db: Session):
    db_user = Users(name = user.name, password = user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

    
def findUser(name: str, password: str, db: Session):
    return db.query(Users).filter(Users.name==name, Users.password == password).first()

def getPassword(password: str, db: Session):
    return db.query

def deleteUser(user: Users, db: Session):
    user_id = user.id
    db.delete(user)
    db.commit()
    return user_id

def findUserById(user_id: int, db: Session):
    return db.query(Users).filter(Users.id==user_id).first()

def update(user_id: int, user: Login, db: Session):
    update_time = datetime.now(timezone.utc)
    db_user = findUserById(user_id, db)
    db_user.name = user.name
    db_user.password = user.password
    db_user.update_at = update_time
    db.commit()
    return db_user