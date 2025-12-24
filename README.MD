# ТЕМА 5.
Разработка веб приложения на тему системы бронирования авиабилетов.


# Для запуска проекта:
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/gewacoba/air_system_web-project.git
   cd air_system_web-project
2.  Создайте и активируйте виртуальное окружение:  
-  Linux/macOS:
    ```bash
   python -m venv venv
   source venv/bin/activate
-  Windows:
    ```bash
   python -m venv venv
   venv\Scripts\activate  
3.  Установите зависимости из файла requirements.txt
    ```bash
    pip install -r requirements.txt
4.  Создать файл .env
    ```bash
    SECRET_KEY=your_secret_key_here
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    DB_NAME=air_system.db
5. Запустите сервер FastAPI:  
    ```bash
   uvicorn main:app
6. Перейти по ссылке:  
http://127.0.0.1:8000/web/index

