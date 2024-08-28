# Blogicum

## Проект django_sprint3

* добавлен Django Debug Toolbar v.4.3.0
* создана учетная запись администратора

      Имя пользователя: admin
      Пароль: pianino1 
 * для изменения пароля учетной записи **admin** используется команда:
        
        ./manage.py changepassword admin 

## Инструкция для пользователей Windows

 1.Клонировать репозиторий и перейти в папку **django_sprint3**:

        git clone git@github.com:Rodomir117/django_sprint3.git
        cd django_sprint3

2.Cоздать и активировать виртуальное окружение:

        py -m venv .venv
        source .venv/Scripts/activate

3.Установить зависимости из файла requirements.txt:

        pip install -r requirements.txt

5.Перейти в папку проекта **blogicum** и запустить его:

        cd blogicum
        ./manage.py migrate
        ./manage.py loaddata db.json 
        ./manage.py runserver

6.Перейти на локальный сервер:

        http://127.0.0.1:8000/

7.Перейти в панель администратора:

       http://127.0.0.1:8000/admin/ 