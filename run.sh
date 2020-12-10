#!/usr/bin/env bash

export FLASK_APP=app/main.py
export FLASK_ENV=development
export FLASK_DEBUG=1

python -m flask run