# Car Rental

Apps:

- Api Car rental

## Prerequisites

* Python3 installed.
* Alternative Docker installed.


## Local Development without Docker

```
sudo apt-get install python3-pip python3-dev build-essential python3-virtualenv virtualenv

virtualenv -p python3 venv

source venv/bin/activate         

cp .dev_env .env                                            

pip install -r requirements.txt 

``` 

### Run migration DB
```
python manage.py makemigrations

python manage.py migrate

```
### Create superuser
```
python manage.py createsuperuser

```

### Run dev server
This will run server on http://localhost:8000
```
python manage.py runserver

```

### Create superuser
If you want, you can create initial super-user with next commad:

```
python manage.py createsuperuser

```

### Running Tests
To run all tests with code-coverate report, simple run:
```
python manage.py test

```

### Running Command DB
To run command to DB, simple run:
```
python manage.py seed_data

```

### Run Local Development with Docker

#### Run Docker compose

```
./up
```

#### Console or for Debugging

```
./up bash
``` 

Run `./devrun` to initialize the server

#### Web

And play! Login to:
http://127.0.0.1:9000/admin/
> user `dev@gmail.com` pass `devdevdev`


#### Tests

```
./up test