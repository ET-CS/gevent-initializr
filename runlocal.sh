#!/usr/bin/env python
import gevent.monkey; gevent.monkey.patch_all()
from bottle import run
from app import routes

run(host='localhost', port=9095, debug=True)

