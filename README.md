# Django_Students_List_PD     
Test site with Django backend. Show add and del students

http://students.patrul36.org:8001/

python3 -m venv venv #Создание вирт окружения (где будут складываться либы)

source venv/bin/activate  #Активация вирт окружения для Mac

pip3 install -r requirements.txt # Cтавим либы в виртуальное окружение

<p>
python3 manage.py makemigrations #Сгенерить sql файл описывающий создание таблиц
</p>

<p>
python3 manage.py migrate #Применить к бд создание таблиц
</p>


echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('userUsername', 'userEmail', 'userPassword')" | python3 manage.py shell #Создаём пользователя для админки *Если не создаётся смени имя пользователя!

Как аналог команда для создания суперюзера - python3 manage.py createsuperuser


python3 manage.py runserver 8000


PS
<p style="background-color:tomato;">Postgres пока не задействован но прописан в докер композе</p>

Акт вирт окруж в джанго прож вин 11
\Django_Students_List_PD\venv\Scripts
.\Activate.ps1

1234567






