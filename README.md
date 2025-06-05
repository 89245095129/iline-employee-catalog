# iline-employee-catalog
Employee database catalog for ILINE GROUP
# Employee Management System

## Описание
Это веб-приложение на Flask для управления данными сотрудников крупной компании. Приложение обеспечивает функциональность для отображения информации о сотрудниках, их поиска и изменения некоторых данных, таких как начальник сотрудника.

## Технологии
- Python 3.7+
- Flask
- Flask-SQLAlchemy
- PostgreSQL
- Git

## Установка и настройка

### Шаг 1: Клонирование репозитория

Клонируйте этот репозиторий на вашу локальную машину:

`bash
git clone https://github.com/ваш_логин/employee-management-system.git
cd employee-management-system


### Шаг 2: Установка зависимостей

Создайте виртуальное окружение:
bash
python -m venv venv

Активируйте виртуальное окружение:

- Windows:
  `bash
  venv\Scripts\activate
  `
- macOS/Linux:
  `bash
  source venv/bin/activate
  `

Установите необходимые библиотеки:
bash
pip install Flask Flask-SQLAlchemy psycopg2-binary

### Шаг 3: Настройка PostgreSQL

1. Установите PostgreSQL, если он еще не установлен. Убедитесь, что служба PostgreSQL запущена.
2. Войдите в PostgreSQL:

   `bash
   psql -U postgres
   `

3. Создайте базу данных employee_db:

   `sql
   CREATE DATABASE employee_db;
   `

4. Выйдите из PostgreSQL:

   `sql
   \q
   `

### Шаг 4: Настройка приложения

Откройте файл app.py и измените строку подключения к базе данных в следующем месте:

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ваш_пароль@localhost/employee_db'


Замените ваш_пароль на пароль, который вы установили для пользователя postgres.

### Шаг 5: Запуск приложения

Запустите приложение:
bash
python app.py

Перейдите в браузере по адресу http://127.0.0.1:5000 для доступа к приложению.

### Шаг 6: Взаимодействие с приложением

- Используйте форму поиска для нахождения сотрудников по имени или фамилии.
- Вы можете изменить начальника сотрудника, введя ID нового начальника в соответствующем поле.

### Шаг 7: Завершение разработки и отправка на GitHub

1. Добавьте все изменения в репозиторий:

   `bash
   git add .
   `

2. Закоммитьте изменения:

   `bash
   git commit -m "Initial commit of the Employee Management System"
   `

3. Отправьте изменения на GitHub:

   `bash
   git push origin main
   ``

