# coding:utf-8
from . import home
from flask import render_template, url_for


@home.route('/')
def index():
    return render_template('index.html')


@home.route('/login')
def login():
    return render_template('login.html')

@home.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')