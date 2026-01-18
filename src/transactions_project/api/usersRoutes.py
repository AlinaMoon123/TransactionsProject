from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from src.transactions_project.services.users import create_user, generate_code, update_user, user_delete, user_login  
from src.transactions_project.db.base import get_db
from src.transactions_project.auth.jwt import get_current_user
from src.transactions_project.db.codeBase import redis_client
from src.transactions_project.services.emailVerefication import check_verification_code, send_verefication_code
from src.transactions_project.core.config import EMAIL_CODE_EXPIRE
from src.transactions_project.schemas.usersSchemas import ActivateUser, CodeInput, CreateUser, TokenResponse, UpdateUser, User, UserId

router = APIRouter(tags=["Пользователь"])


@router.post('/register', response_model=User)
async def register(user: CreateUser , background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):
    db_user = await create_user(user, db)
    code = generate_code()
    await redis_client.setex(
        f'verify:{db_user.email}',
        EMAIL_CODE_EXPIRE,
        code
    )

    background_tasks.add_task(
        send_verefication_code,
        user.email,
        code
    )
    return db_user


@router.get('/user', response_model=User)
async def get_user(current_user: User = Depends(get_current_user), db: AsyncSession=Depends(get_db)):
    return current_user


@router.post('/login', response_model=TokenResponse)
async def login(form_data: OAuth2PasswordRequestForm=Depends(), db: AsyncSession=Depends(get_db)):
    token = await user_login(form_data.username, form_data.password, db)
    return token
    

@router.patch('/user', response_model=User)
async def update(user: UpdateUser, current_user: User=Depends(get_current_user), db:AsyncSession=Depends(get_db)):
    db_user = await update_user(current_user.id, user,  db)
    return db_user


@router.delete('/user', response_model=UserId)
async def delete_user(current_user: User = Depends(get_current_user), db: AsyncSession=Depends(get_db)):
    deleted_user_id = await user_delete(current_user.id, db)
    return {"id": deleted_user_id}


@router.patch('/verify-email', response_model=ActivateUser)
async def activate_user(code: CodeInput, db: AsyncSession=Depends(get_db)):
    await check_verification_code(code.email, code.code, db)
    return {"message": "Email successfully verified"}