# REST API для управления пользователями и финансовыми транзакциями

REST API для управления пользователями и финансовыми транзакциями с поддержкой JWT-аутентификации, подтверждением регистрации по email и полным CRUD операциями.

## Оглавление

- [Основные возможности](#основные-возможности)
- [Технологии](#технологии)
- [Архитектура и ERD](#архитектура-и-erd)
- [Структура базы данных](#структура-базы-данных)
---
## Основные возможности

- **Регистрация и аутентификация** с JWT-токенами
- **Подтверждение email** через код (хранится в Redis)
- **CRUD операции** над транзакциями
- **Связи:** пользователь → транзакции, типы транзакций → транзакции
- **Валидация** данных через Pydantic
- **Docker Compose** для развёртывания (FastAPI + PostgreSQL + Redis)

  ## Технологии

| Компонент       | Технология                                          |
|----------------|-----------------------------------------------------|
| **Язык**       | Python                                              |
| **Фреймворк**  | FastAPI                                             |
| **ORM**        | SQLAlchemy                                          |
| **Валидация**  | Pydantic v2                                         |
| **База данных**| PostgreSQL                                          |
| **Коды**       | Redis                                               |
| **JWT**        | python-jose (HS256)                                 |
| **Хеширование**| passlib[bcrypt]                                     |
| **Email**      | smtplib                                             |
| **Контейнеры** | Docker, Docker Compose                              |

## Структура базы данных

### Users

| Поле        | Тип        | Описание |
|-------------|------------|----------|
| id          | Integer (PK) | Уникальный идентификатор аккаунта |
| name        | String, nullable=False | Имя пользователя |
| password    | String, nullable=False | Пароль |
| created_at  | DateTime, default=datetime.utcnow | Дата создания |
| updated_at  | DateTime, nullable=True | Дата последнего обновления |

---

### TransactionTypes

| Поле        | Тип        | Описание |
|-------------|------------|----------|
| id          | Integer (PK) | Уникальный идентификатор типа |
| name        | String, nullable=False | Название типа (платёж, перевод и т.д.) |
| description | String, nullable=True | Описание |
| created_at  | DateTime, default=datetime.utcnow | Дата создания |

---

### Transactions

| Поле        | Тип        | Описание |
|-------------|------------|----------|
| id          | Integer (PK) | Уникальный идентификатор транзакции |
| user_id     | Integer (FK → Users.id) | Пользователь |
| type_id     | Integer (FK → TransactionTypes.id) | Тип транзакции |
| amount      | Numeric, nullable=False | Сумма |
| category    | String, nullable=False | Категория (еда, транспорт и т.д.) |
| created_at  | DateTime, default=datetime.utcnow | Дата создания |
| status      | String, nullable=False | Статус (успешно, отклонено и т.д.) |




## ER diagramm
![ERD.png](https://github.com/AlinaMoon123/TransactionsProject/blob/main/ERD.png)


