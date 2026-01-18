from datetime import datetime
from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel, field_validator, model_validator

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

    @field_validator("name", "email", "password")
    @classmethod
    def not_empty_fields(cls, value: Optional[str]):
        if value is None:
            return value
        if not value.strip():
            raise HTTPException(status_code=400, detail="Fields cannot be empty")
        return value

    @model_validator(mode="after")
    def at_least_one_not_empty(self):
        fields = any([self.name is not None, self.email is not None, self.password is not None])
        if not fields:
            raise HTTPException(status_code=400, detail="At least one field must be provided")
        return self
           
# TODO написать кастомный валидатор (@field_validator) и если ничего не ввёл то 400 Bad Request

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ActivateUser(BaseModel):
    message: str 

class CodeInput(BaseModel):
    email: str
    code: str
