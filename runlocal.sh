#!/usr/bin/env python
from bottle import run
from app import routes

run(host='localhost', port=9095, debug=True)

