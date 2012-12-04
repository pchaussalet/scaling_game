#!/bin/bash
uwsgi --http-socket :5000 -H venv -w app:app -p 4 --threads 1 --enable-threads
