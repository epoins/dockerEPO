docker build -t appvol .
mkdir dir

docker run --rm --name myappvol \ 
-v myvol:/named -v $(pwd)/dir:/bind --tmpfs /tmpfs \ 
-d -it appvol

docker volume ls

touch dir/local
docker exec -it myappvol bash
ls /bind
ls /named
exit

docker stop myappvol 
docker volume ls
