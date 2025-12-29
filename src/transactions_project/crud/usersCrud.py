from datetime import timezone
from src.transactions_project.schemas.usersSchemas import *
from sqlalchemy.orm import Session
from src.transactions_project.models.users import Users
from src.transactions_project.models import users

def create(user: CreateUser, db: Session):
    db_user = Users(name = user.name, password = user.password, email = user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

    
def findUser(email: str, password: str, db: Session):
    return db.query(Users).filter(Users.email==email, Users.password == password).first()

# def getPassword(password: str, db: Session):
#     return db.query

def deleteUser(user: Users, db: Session):
    user_id = user.id
    db.delete(user)
    db.commit()
    return user_id

def findUserById(user_id: int, db: Session):
    return db.query(Users).filter(Users.id==user_id).first()

def findSameEmail(user_id: int, email: str, db: Session):
    return db.query(Users).filter(Users.id!=user_id, Users.email==email).first()

def findEmail(email: str, db: Session):
    return db.query(Users).filter(Users.email==email).first()

def update(user_id: int, user: UpdateUser, db: Session):
    db_user = findUserById(user_id, db)
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
    db.commit()
    db.refresh(db_user)
    return db_user

def activateUser(email: int, db: Session):
    db_user = findEmail(email, db)
    db_user.is_active = True
    db.commit()
    return db_user