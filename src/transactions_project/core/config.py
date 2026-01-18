import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

EMAIL_CODE_EXPIRE=int(os.getenv("EMAIL_CODE_EXPIRE_MINUTES")) * 60

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL_SYNC=os.getenv("DATABASE_URL_SYNC")

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))

SMTP_HOST=os.getenv("SMTP_HOST")
SMTP_PORT=int(os.getenv("SMTP_PORT"))
SMTP_USER=os.getenv("SMTP_USER")
SMTP_PASSWORD=os.getenv("SMTP_PASSWORD")
