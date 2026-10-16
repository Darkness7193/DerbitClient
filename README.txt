uv sync

mv example.env .env

sudo docker compose up --build -d

sudo docker compose exec rabbitmq rabbitmqctl add_user rabbitmquser password

sudo docker compose exec rabbitmq rabbitmqctl set_permissions -p / rabbitmquser ".*" ".*" ".*"

uv run alembic revision --autogenerate -m "__init__"

sudo docker compose exec -it app uv run alembic upgrade head

sudo docker compose up --build