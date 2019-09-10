#!/bin/bash

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/guni.conf /etc/gunicorn.d/django
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start

