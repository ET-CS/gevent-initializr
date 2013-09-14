#!/usr/bin/env python
from bottle import route, redirect, get, post, request
from bottle import static_file
from bottle import template

import tenjin
from tenjin.helpers import *

import os; currentpath=os.path.dirname(os.path.abspath(__file__))

@route('/')
def index():
    context = {
        'project': 'gevent-initializr',
        'title': 'Hello, world!',
    }
    engine = tenjin.Engine(path=['app/views'])
    html = engine.render('index.pyhtml', context)
    return html

@route('/css/<filename>')
def server_static(filename):
    return static_file(filename, root=currentpath+'/static/css')

@route('/js/<filename>')
def server_static(filename):
    return static_file(filename, root=currentpath+'/static/js')

@route('/images/<filename>')
def server_static(filename):
    return static_file(filename, root=currentpath+'/static/images')
