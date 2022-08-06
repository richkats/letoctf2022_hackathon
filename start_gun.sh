#!/bin/bash

git pull
cd ~/letoctf2022_hackathon/backend
lsof -ti tcp:5000 | xargs kill
gunicorn --bind 0.0.0.0:5000 wsgi:app &