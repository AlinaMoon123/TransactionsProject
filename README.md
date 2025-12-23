# REST API для управления пользователями и финансовыми транзакциями

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


