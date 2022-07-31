# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
#EXPOSE 8001
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]