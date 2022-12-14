Проект предоставляет возможность подключаться к социальной сети Yatube по API.
Можно получать и изменять посты, группы и комментарии.

Пользователи могут регистрироваться и изменять пароли по необходимости.

Написано на REST Framework и python 3.

Как использовать. Сначала надо установить python. Потом устанавливаем django.
```BASH
$ pip install django
```
Потом клонируем репозиторий себе на компьютер:
```BASH
$ git clone git@github.com/USERNAME/{{ project_name }}.git
```
Переходим в папку проекта $ cd {{ project_name }}

Создаем и активируем виртуальное пространство
```BASH
python -m venv venv source venv/Scripts/activate
```
Устанавливаем все необходимые пакеты:
```BASH
$ pip install -r requirements/local.txt
```
Создаем миграции:
```BASH
$ python manage.py makemigrations
$ python manage.py migrate
```
И теперь можно запускать сервер:
```BASH
$ python manage.py runserver
```
Для чтения документации по API можно перейти по ссылке http://127.0.0.1:8000/redoc/

Для доступа в админку надо перейти на http://127.0.0.1:8000/admin

Автор: Бражинский Валерий.


