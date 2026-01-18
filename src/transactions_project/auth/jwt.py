from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from src.transactions_project.crud.usersCrud import findUserById
from src.transactions_project.db.base import get_db
from src.transactions_project.core.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire_time = datetime.now(timezone.utc) + expires_delta
    else:
        expire_time = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire_time})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_jwt

def create_access_token(user_id: int):
    data = {"sub": str(user_id), "type": "access"}
    access_token = create_token(data)
    return access_token

async def get_current_user(db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != "access":
            raise HTTPException(status_code=401, detail="Invalid token type")
        user_id = int(payload.get("sub"))
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid or expired token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    db_user = await findUserById(user_id, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user   

    

