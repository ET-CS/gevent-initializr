#!/usr/bin/env python
from bottle import run
from app import routes

run(host='0.0.0.0', port=9095, debug=True, reloader=True)
