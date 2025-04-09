# Wayu

## Project setup

`` virtualenv venv``

### Actual virtual environmen

`` source venv/bin/activate ``

### Configure Environment files

`` cp .env.examples .env ``

### Install dependencies

`` pip install -r requirements/develop.txt  ``

###  Install pre-commit

`` pre-commit install ``


## Run migration

`` python manage.py migrate ``

### Run project

```

python  manage.py createsuperuser
python manage.py runserver

```
