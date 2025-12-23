from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Login(BaseModel):
    name: str
    password: str

class CreateUser(Login):
    submit_password: str

class User(Login):
    id: int
    created_at: datetime
    update_at: Optional[datetime] = None

class UserId(BaseModel):
    id: int

class UpdateUser(Login):
    id: int

