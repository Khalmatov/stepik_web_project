#!/bin/bash

sudo /etc/init.d/mysql start
mysql -uroot -e "create database webdb;"
mysql -uroot -e "grant all privileges on webdb.* to 'box'@'localhost' with grant option;"

~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/guni.conf /etc/gunicorn.d/django
sudo /etc/init.d/gunicorn restart