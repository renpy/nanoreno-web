#!/bin/bash

# set -x

cd $HOME

rm virtualenv.$1/bin/python

cp /usr/bin/python3.4 virtualenv.$1/bin/python
cp /usr/bin/python3.4 virtualenv.$1/bin/python3
cp /usr/bin/python3.4 virtualenv.$1/bin/python3.4
cp /usr/bin/python3.4 virtualenv.$1/bin/python3.4mu

touch wsgi.$1/main.wsgi
