
from fastapi import FastAPI
from src.transactions_project.db.base import Base
from src.transactions_project.api.usersRoutes import router as user_router
from src.transactions_project.models import *
from src.transactions_project.db.base import engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(user_router)

