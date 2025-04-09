.PHONY: install
install:
	poetry install


.PHONY: migrate
migrate:
	poetry run python manage.py migrate


.PHONY: migrations
migrations:
	poetry run python manage.py makemigrations


.PHONY: run-server
run-server:
	poetry run python manage.py runserver


.PHONY: superuser
superuser:
	poetry run python manage.py createsuperuser



