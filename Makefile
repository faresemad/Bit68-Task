COMPOSE_FILE = docker-compose-dev.yml

up:
	docker-compose -f $(COMPOSE_FILE) up -d

build:
	docker-compose -f $(COMPOSE_FILE) build

restart:
	docker-compose -f $(COMPOSE_FILE) restart

down:
	docker-compose -f $(COMPOSE_FILE) down

stop:
	docker-compose -f $(COMPOSE_FILE) stop

destroy:
	docker-compose -f $(COMPOSE_FILE) down --rmi all

logs:
	docker-compose -f $(COMPOSE_FILE) logs $(filter-out $@,$(MAKECMDGOALS))

makemigrations:
	docker-compose -f $(COMPOSE_FILE) run --rm djweb python manage.py makemigrations

migrate:
	docker-compose -f $(COMPOSE_FILE) run --rm djweb python manage.py migrate $(filter-out $@,$(MAKECMDGOALS))

createsuperuser:
	docker-compose -f $(COMPOSE_FILE) run --rm djweb python manage.py createsuperuser

shell:
	docker-compose -f $(COMPOSE_FILE) run --rm djweb python manage.py shell

test:
	docker-compose -f $(COMPOSE_FILE) run --rm djweb python manage.py test

startapp:
	docker-compose -f $(COMPOSE_FILE) run --rm djweb python manage.py startapp $(filter-out $@,$(MAKECMDGOALS))

collectstatic:
	docker-compose -f $(COMPOSE_FILE) run --rm djweb python manage.py collectstatic