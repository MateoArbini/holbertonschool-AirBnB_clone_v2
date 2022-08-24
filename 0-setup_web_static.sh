#!/usr/bin/env bash
#Bash script that sets up your web server for the deplyment of web static.

sudo apt update
sudo apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "54i /server_name _;/a location /static/ {\n \talias /data/web_static/current/; \n\tautoindex off; \n}" /etc/nginx/sites-enabled/default
sudo service nginx restart
