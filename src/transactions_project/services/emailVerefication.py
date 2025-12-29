from email.message import EmailMessage
import os
import smtplib
from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.transactions_project.db.tokenBase import redis_client
from src.transactions_project.crud.usersCrud import activateUser

SMTP_HOST=os.getenv("SMTP_HOST")
SMTP_PORT=int(os.getenv("SMTP_PORT"))
SMTP_USER=os.getenv("SMTP_USER")
SMTP_PASSWORD=os.getenv("SMTP_PASSWORD")

def send_email(to_email: str, subject: str, body: str):
    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10) as server:
        server.starttls()            
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)

def send_verefication_code(to_email: str, code: str):
    subject = "Verefication Code"
    body = f"""
            Здравствуйте!

            Ваш код подтверждения регистрации:

            {code}

            Код действует 15 минут.
            """
    send_email(to_email, subject, body)


def check_verification_code(email: str, code: str, db: Session):
    stored_code = redis_client.get(f'verify:{email}')
    if stored_code == None:
        raise HTTPException(status_code=400, detail="Verification code expired")
    if stored_code == code:
        db_user = activateUser(email, db)
        redis_client.delete(email)
        return db_user
    raise HTTPException(status_code=400, detail="The code is wrong! Try again!")

