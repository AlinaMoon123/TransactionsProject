from fastapi import APIRouter, Depends
from src.transactions_project.services.users import *
from src.transactions_project.db.base import get_db

router = APIRouter()


@router.post('/register', response_model=User)
def register(user: CreateUser , db: Session = Depends(get_db)):
    db_user = create_user(user, db)
    return db_user


@router.get('/user/{user_id}')
def get_user(user_id: int, db: Session =Depends(get_db)):
    db_user = get_user_by_id(user_id, db)
    return db_user

@router.post('/login', response_model=User)
def login(user: Login , db: Session = Depends(get_db)):
    db_user = user_login(user, db)
    return db_user
    

@router.patch('/user/{user_id}')
def update(user_id: int, user: Login, db: Session =Depends(get_db)):
    db_user = update_user(user_id, user,  db)
    return db_user


@router.delete('/user', response_model = UserId)
def delete_user(user_id: int , db: Session = Depends(get_db)):
    deleted_user_id = user_delete(user_id, db)
    return {"id": deleted_user_id}





