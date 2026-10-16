uv sync

Установить rabbitmq пользователя, дать ему права, проверить его наличие, перезапустить контейнер:

    sudo docker compose exec rabbitmq rabbitmqctl add_user rabbitmquser password

    sudo docker compose exec rabbitmq rabbitmqctl set_permissions -p / rabbitmquser ".*" ".*" ".*"

    sudo docker compose exec rabbitmq rabbitmqctl list_users

    sudo docker compose up -d --force-recreate app

sudo docker compose up -d app

sudo docker compose exec app uv run alembic init migrations

sudo docker compose exec app uv run alembic revision --autogenerate -m "__init__"

sudo docker compose exec app uv run alembic upgrade head

sudo docker compose up --build