# REST API для управления пользователями и финансовыми транзакциями

## Описание проекта

Необходимо разработать REST API для управления пользователями и их финансовыми транзакциями с использованием:

- **Python**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic**

Приложение должно обеспечивать:
- регистрацию и аутентификацию пользователей;
- CRUD-операции для транзакций;
- валидацию входящих и исходящих данных;
- структурированное хранение данных с учётом связей между сущностями;
- безопасный и понятный API.

---

## Основные задачи

1. Спроектировать **ERD (Entity-Relationship Diagram)**.
2. Создать **SQLAlchemy-модели** в декларативном стиле.
3. Реализовать **CRUD-логику**:
   - для пользователей;
   - для транзакций.
4. Создать **API endpoints**:
   - пользователи: регистрация, аутентификация;
   - транзакции: создание, чтение, обновление, удаление.
5. Создать **Pydantic-схемы**:
   - для запросов (Request schemas);
   - для ответов (Response schemas).

---

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

---

## Связи между таблицами

- **Users ↔ Transactions**  
  *One-to-Many*  
  Один пользователь может иметь несколько транзакций.

- **TransactionTypes ↔ Transactions**  
  *One-to-Many*  
  Один тип транзакции может использоваться во многих транзакциях.



## ER diagramm
![ERD.png](https://github.com/AlinaMoon123/TransactionsProject/blob/main/ERD.png)

