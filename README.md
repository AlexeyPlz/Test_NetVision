# Тестовое "Net Vision"
## Автор
- [AlexeyPlz](https://github.com/AlexeyPlz)
## Проверка проекта
[![Flake8](https://github.com/AlexeyPlz/Test_NetVision/actions/workflows/codestyle.yml/badge.svg)](https://github.com/AlexeyPlz/Test_NetVision/actions/workflows/codestyle.yml)
## Стек
- Python 3.10
- FastAPI 0.98
- FastAPI REST 0.4.5
- SQLAlchemy 2.0.17
- PostgreSQL 13.2
- Asyncpg 0.27
- Alembic 1.11.1
- Uvicorn 0.22
- Aiohttp 3.8.4
## Задание
Используя Python3, FastAPI, SQLAlchemy написать:
- REST API сервер
- Клиентское приложение

### Веб-приложение (микросервис)
Необходимо реализовать следующие endpoint:
- POST `/new`

    Сохраняет запись в базу данных и присваивает ей уникальный идентификатор uuid. Пример тела запроса:
    ```json
    [
        {"uuid": "e48d41d0-6e53-490a-9d9a-fd4337f28038", "text": "test example"},
        {"uuid": "eddd8cd7-1128-4b83-98d4-7cde1514625e", "text": "another example"}
    ]
    ```

-  GET `/all`

    Отдаёт все добавленные записи, пример тела ответа:
    ```json
    [
        {"uuid": "e48d41d0-6e53-490a-9d9a-fd4337f28038", "text": "test example"},
        {"uuid": "eddd8cd7-1128-4b83-98d4-7cde1514625e", "text": "another example"}
    ]
    ```

- GET `/<uuid>`

    Отдаёт конкретную запись по запрошенному uuid. Если записи не существует, отдаёт HTTP 404. Пример успешного ответа:
    ```json
    {"uuid": "e48d41d0-6e53-490a-9d9a-fd4337f28038", "text": "test example"}
    ```

- GET `/<count>`

    Отдаёт запрошенное в <count> количество записей. Пример успешного ответа:
    ```json
    [
        {"uuid": "e48d41d0-6e53-490a-9d9a-fd4337f28038", "text": "test example"},
        {"uuid": "eddd8cd7-1128-4b83-98d4-7cde1514625e", "text": "another example"}
    ]
    ```

- DELETE `/<uuid>`

    Удаляет запись по запрошенному uuid из базы. Если записи не существует, отдаёт HTTP 404. В случае успеха возвращает HTTP 200.

### Клиентское приложение (микросервис)
Запускается вместе с первым и постоянно генерирует случайное количество (от 10 до 100) случайных строк (буквы-цифры, 16 символов) для вставки в базу первого сервиса по API.  
Одновременно с этим приложение постоянно запрашивает по API по 10 строк и удаляет их, раз в 10 секунд в стандартный поток вывода необходимо печать количество удалённых записей.  
## Запуск локально
- ToDo
