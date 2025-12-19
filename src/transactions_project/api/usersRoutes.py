from fastapi import APIRouter, Depends
from src.transactions_project.services.users import *
from src.transactions_project.db.base import get_db

router = APIRouter()


@router.post('/register', response_model=User)
def register(user: CreateUser , db: Session = Depends(get_db)):
    db_user = create_user(user, db)
    return db_user


@router.get('/user')
def login():
    pass


@router.patch('/user')
def update():
    pass


@router.delete('/user')
def delete_user():
    pass





