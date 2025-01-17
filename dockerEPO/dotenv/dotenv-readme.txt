Objective: 
Deploy a simple web application using Docker Compose, 
ensuring that sensitive configuration data (such as database credentials) is managed securely using a .env file.

Tools:

Docker
Docker Compose
A simple web application (e.g., a Flask app)
A database (e.g., PostgreSQL)


Provided files:

my.env contains the keywords to connect to the database

app.py will read this keywords

requirements.txt contains extra software list

Dockerfile start python app.py and will use the requirements.txt 

compose.yaml will start 2 services : db and then web



RUN: 
docker compose up --build

Check :
curl http://localhost:5000
or 
lynx http://localhost:5000

you shoud see the db version:
Database version: ('PostgreSQL 13.18 (Debian 13.18-1.pgdg120+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit',)

Stop :
docker compose down

-------------------------------------
Run better in background :
docker compose up -d --build

