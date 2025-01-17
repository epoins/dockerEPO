cd exo6
Create a compose.yaml to start 2 applications :

php:7.4-apache 
Port 8080 is external
Local volume ./html  is in the app : /var/www/html
Launch command to install mysqli  : sh -c "docker-php-ext-install mysqli && apache2-foreground"

mysql:5.7
Env: 
MYSQL_ROOT_PASSWORD: rootpassword
MYSQL_DATABASE: myapp
MYSQL_USER: user
MYSQL_PASSWORD: password

Bind Volumes:
./mysql-data is in the app /var/lib/mysql
./init.sql  is in the app  /docker-entrypoint-initdb.d/init.sql

The program init.sql and html/index.html are provided.
Start the services and check the web
