sudo docker compose exec rabbitmq rabbitmqctl add_user rabbitmquser password

sudo docker compose exec rabbitmq rabbitmqctl set_permissions -p / rabbitmquser ".*" ".*" ".*"

sudo docker compose exec rabbitmq rabbitmqctl list_users

sudo docker compose up -d --force-recreate app