
clean: destroy migrate build up seed_db

create_superuser:
	docker-compose -f local.yml run --rm django python manage.py createsuperuser

destroy:
	docker-compose -f local.yml down -v

build:
	docker-compose -f local.yml build

build_nocache:
	docker-compose -f local.yml build --no-cache

up:
	docker-compose -f local.yml up -d

test-cover:
	docker-compose -f local.yml run --rm django sh -c "pytest --cov-report html --durations=0 --cov --no-cov-on-fail --disable-warnings"

test:
	docker-compose -f local.yml run --rm django sh -c "pytest -s"

shell:
	docker-compose -f local.yml run --rm django sh -c "python manage.py shell_plus"

migrations:
	docker-compose -f local.yml run --rm django sh -c "python manage.py makemigrations"

migrate:
	docker-compose -f local.yml run --rm django sh -c "python manage.py migrate"
