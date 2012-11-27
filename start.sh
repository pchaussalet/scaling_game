#!/bin/bash
uwsgi --http-socket :5000 -H venv -w app:app -p 4 --enable-threads
