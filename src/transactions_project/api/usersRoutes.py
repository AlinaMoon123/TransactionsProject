import os
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.transactions_project.services.users import *
from src.transactions_project.db.base import get_db
from src.transactions_project.auth.jwt import get_current_user
from src.transactions_project.db.tokenBase import redis_client
from src.transactions_project.services.emailVerefication import check_verification_code, send_verefication_code

router = APIRouter()
EMAIL_CODE_EXPIRE=int(os.getenv("EMAIL_CODE_EXPIRE_MINUTES")) * 60

@router.post('/register', response_model=User)
def register(user: CreateUser , db: Session = Depends(get_db)):
    db_user = create_user(user, db)
    code = generate_code()
    redis_client.setex(
        f'verify:{db_user.email}',
        EMAIL_CODE_EXPIRE,
        code
    )
    send_verefication_code(user.email, code)
    return db_user


@router.get('/user', response_model=User)
def get_user(current_user: User = Depends(get_current_user), db: Session =Depends(get_db)):
    return current_user

@router.post('/login', response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(get_db)):
    token = user_login(form_data.username, form_data.password, db)
    return token
    

@router.patch('/user', response_model=User)
def update( user: UpdateUser, current_user: User = Depends(get_current_user), db: Session =Depends(get_db)):
    db_user = update_user(current_user.id, user,  db)
    return db_user


@router.delete('/user', response_model = UserId)
def delete_user(current_user: User = Depends(get_current_user) , db: Session = Depends(get_db)):
    deleted_user_id = user_delete(current_user.id, db)
    return {"id": deleted_user_id}

@router.patch('/verify-email', response_model=ActivateUser)
def activate_user(code: CodeInput, db: Session = Depends(get_db)):
    check_verification_code(code.email, code.code, db)
    return {"message": "Email successfully verified"}




