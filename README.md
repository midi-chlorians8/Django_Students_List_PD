# Django_Students_List_PD     
Test site with Django backend. Show add and del students

python -m venv venv #Создание вирт окружения (где будут складываться либы)

source venv/bin/activate  #Активация вирт окружения для Mac

pip install -r requirements.txt # Cтавим либы в виртуальное окружение

python3 manage.py makemigrations #Сгенерить sql файл описывающий создание таблиц
python3 manage.py migrate #Применить к бд создание таблиц

python3 manage.py runserver 8002
