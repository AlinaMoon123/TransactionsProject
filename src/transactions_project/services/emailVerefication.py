from email.message import EmailMessage
import aiosmtplib
from sqlalchemy.ext.asyncio import AsyncSession
from src.transactions_project.db.codeBase import redis_client
from src.transactions_project.crud.usersCrud import activateUser
from src.transactions_project.core.exception import CustomExc
from src.transactions_project.core.config import SMTP_HOST, SMTP_PASSWORD, SMTP_PORT, SMTP_USER

async def send_email(to_email: str, subject: str, body: str):
    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    server = aiosmtplib.SMTP(
    hostname=SMTP_HOST,
    port=SMTP_PORT,
    timeout=10
    )

    await server.connect()
    await server.login(SMTP_USER, SMTP_PASSWORD)
    await server.send_message(msg)
    await server.quit()


async def send_verefication_code(to_email: str, code: str):
    subject = "Verefication Code"
    body = f"""
            Здравствуйте!

            Ваш код подтверждения регистрации:

            {code}

            Код действует 15 минут.
            """
    await send_email(to_email, subject, body)


async def check_verification_code(email: str, code: str, db: AsyncSession):
    stored_code = await redis_client.get(f'verify:{email}')
    if stored_code == None:
        raise CustomExc(status_code=400, detail="Verification code expired")
    if stored_code == code:
        db_user = await activateUser(email, db)
        await redis_client.delete(email)
        return db_user
    raise CustomExc(status_code=400, detail="The code is wrong! Try again!")

