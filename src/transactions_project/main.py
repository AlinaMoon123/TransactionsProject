
from fastapi import FastAPI
from src.transactions_project.db.base import Base
from src.transactions_project.api.usersRoutes import router as user_router
from src.transactions_project.api.transactionTypesRoutes import router as type_router
from src.transactions_project.api.transactionsRoutes import router as transaction_router
from src.transactions_project.models.transactionTypes import TransactionTypes
from src.transactions_project.models.transactions import Transactions
from src.transactions_project.models.users import Users
from src.transactions_project.db.base import engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(type_router)
app.include_router(transaction_router)


