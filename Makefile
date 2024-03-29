# DOCKER DEPLOY ------------------------------------------------
file := "docker-compose.yml"

up:
	# Create and start containers
	docker-compose up -d db
	sleep 10
	docker-compose up -d api
	docker-compose logs -f

build:
	# Rebuild the docker compose
	docker-compose build

restart:
	# Restart services
	docker-compose restart

logs:
	# View output from containers
	docker-compose logs

start:
	# Start services
	docker-compose start

stop:
	# Stop services
	docker-compose stop

ps:
	# List all running containers
	docker-compose ps

down:
	# Stop and Remove all containers
	docker-compose down

migrations:
	# Create migrations
	docker-compose run api python manage.py makemigrations

migrate:
	# Migrate migrations
	sudo docker-compose up -d
	sudo docker exec -it restaurant-service python manage.py makemigrations
	sudo docker exec -it restaurant-service python manage.py migrate
	sudo docker-compose logs -f

test:
	# run unit tests
	docker-compose run api python manage.py test
