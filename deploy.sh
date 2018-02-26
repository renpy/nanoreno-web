#!/bin/bash

set -e

grunt build

user=tom
host=erika
site=nanoreno
virtualenv=nanoreno

ssh $user@$host mkdir -p /home/$user/virtualenv.$site
ssh $user@$host mkdir -p /home/$user/wsgi.$site
ssh $user@$host mkdir -p /home/$user/WWW.$site

# rsync -av --delete ~/.virtualenvs/$virtualenv/ $user@$host:/home/$user/virtualenv.$site --exclude __pycache__

sync () {
    rsync -av --delete $1 $user@$host:/home/$user/wsgi.$site --exclude __pycache__
}

sync dist
sync flask_yeoman.py
sync main.py
sync main.wsgi
sync web
sync after-deploy.sh

ssh $user@$host /home/$user/wsgi.$site/after-deploy.sh $site

