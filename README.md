# Django_Students_List_PD     
Test site with Django backend. Show add and del students

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








<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>
