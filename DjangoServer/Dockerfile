FROM python:3.9

WORKDIR /django_web

COPY . .
COPY requirements.txt requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]