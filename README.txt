uv sync

Переименовать example.env в .env

sudo docker compose up --build -d

sudo docker compose exec rabbitmq rabbitmqctl add_user rabbitmquser password

sudo docker compose exec rabbitmq rabbitmqctl set_permissions -p / rabbitmquser ".*" ".*" ".*"

sudo docker compose exec app uv run alembic upgrade head

sudo docker compose up --build