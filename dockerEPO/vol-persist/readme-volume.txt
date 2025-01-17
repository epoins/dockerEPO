Named volume for 2 containers:
docker volume create myvol
docker run -it --name ubuntu1 -v myvol:/tmp -d ubuntu /bin/bash
docker run -it --name ubuntu2 -v myvol:/tmp -d ubuntu /bin/bash
docker exec -it ubuntu1 /bin/bash
touch /tmp/toto.txt
exit
docker exec -it ubuntu2 /bin/bash
ls /tmp; echo hello > /tmp/toto.txt
docker rm -f ubuntu1

3rd container:
docker run -it --name ubuntu3  -v myvol:/tmp -d ubuntu /bin/bash
docker exec -it ubuntu3 /bin/bash
cat /tmp/toto.txt

