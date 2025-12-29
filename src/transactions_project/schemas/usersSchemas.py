from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Login(BaseModel):
    email: str
    password: str

class CreateUser(Login):
    submit_password: str
    name: str

class User(Login):
    id: int
    name: str
    created_at: datetime
    update_at: Optional[datetime] = None
    is_active: bool

class UserId(BaseModel):
    id: int

class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ActivateUser(BaseModel):
    message: str 

class CodeInput(BaseModel):
    email: str
    code: str
