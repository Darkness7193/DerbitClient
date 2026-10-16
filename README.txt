uv sync &&

mv example.env .env &&



sudo docker compose up --build

sudo docker compose exec rabbitmq rabbitmqctl add_user rabbitmquser password &&

sudo docker compose exec rabbitmq rabbitmqctl set_permissions -p / rabbitmquser ".*" ".*" ".*" &&

sudo docker compose exec -it app uv run alembic upgrade head &&

sudo docker compose up --build