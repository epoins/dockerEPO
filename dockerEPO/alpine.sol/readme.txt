Find the alpine:latest image on the web
https://hub.docker.com/_/alpine

Download the version latest 
docker pull alpine:latest

Run this image on your machine, in background, and give it a name like myalpine
docker run -d  -it --name myalpine alpine sh

Check the container is correctly running
docker ps

Connect to the container and get the file /etc/os-release
docker exec -it myalpine sh
cat /etc/os-release

Stop the container and verify
exit (from sh)

docker stop myalpine
docker ps
