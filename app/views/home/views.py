#coding:utf-8
from . import home
from flask import render_template, url_for

@home.route('/')
def index():
    return render_template('base.html')