
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.transactions_project.db.base import Base
from src.transactions_project.api.usersRoutes import router as user_router
from src.transactions_project.api.transactionTypesRoutes import router as type_router
from src.transactions_project.api.transactionsRoutes import router as transaction_router
from src.transactions_project.db.base import engine

app = FastAPI()

app.include_router(user_router)
app.include_router(type_router)
app.include_router(transaction_router)

