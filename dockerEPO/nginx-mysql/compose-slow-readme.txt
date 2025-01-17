Let’s process slowly:
cd nginx-mysql
docker compose build db
docker compose create db

Check: (nothing)
docker compose ls
docker compose images

Start the container
docker compose start db

Check again:
docker compose ls
docker compose images
docker [compose] ps
