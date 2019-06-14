#!/usr/bin/env bash

echo "DB MIGRATE"
until python manage.py migrate
  do
      echo "UPGRADE: Waiting for postgres ready..."
      sleep 2
  done

python manage.py runserver 0.0.0.0:8000