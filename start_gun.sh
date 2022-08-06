#/bin/bash

git pull
cd ~/letoctf2022_hackathon/backend
gunicorn --bind 0.0.0.0:5000 wsgi:app