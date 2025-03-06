## Simple Book Management API

FastAPI-приложение моделирует библиотеку книг. Функционал включает в себя добавление новых книг, получение полного списка, просмотр подробной информации о конкретной книге, редактирование данных книги и удаление книг из библиотеки.

### Endpoints:
> GET /books - Получить список всех книг. Скрытые параметры запроса: _offset_, _limit_ - для ограничения выдачи
> _search_ - поиск вхождения в атрибуты книги _title_, _author_, _publisher_.<br>
> 


>POST /books - Добавить новую книгу.<br>
GET /books/{book_id} - Получить подробную информацию о книге.<br>
PUT /books/{book_id} - Обновить информацию о книге.<br>
DELETE /books/{book_id} - Удалить книгу.


### Модель объекта книги
```python
class Book:
    book_id: str  # Идентификатор книги
    title: str  # Наименование книги
    author: str  # Автор книги
    year: int  # Год издания книги
```

Список книг хранится в файле books_db.py в виде списка словарей.

---
## Установка и запуск

### Склонировать проект

`git clone https://github.com/IT-Arkhipov/books_managment_api.git`

Перейти в папку, создать виртуальное окружение и установить зависимости (предварительно установлен python):
> cd books_managment_api<br>

### 1. Запуск проекта вручную
> python -m venv venv<br>
> .\venv\Scripts\activate<br>
> pip install -r requirements.txt<br>
> python main.py

API-сервер: `127.0.0.1:8000`, Swagger: [http:\\127.0.0.1:8000\docs](http:\\127.0.0.1:8000\docs)

### 2. Запуск проекта через Docker
> docker build . -t books_api<br>
> docke run --rm -p 8000:8000 books_api