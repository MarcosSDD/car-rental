FROM python:3.9.14

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
COPY requirements.txt /usr/src/app/

RUN apt-get -qq update && \
    apt-get install -qq -y gettext && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV DJANGO_SETTINGS_MODULE=car_rental.settings

RUN python manage.py migrate
#python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["gunicorn", "car_rental.wsgi:application", "--bind", "0.0.0.0:8000"]