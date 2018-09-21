# coding:utf-8
import os
from flask import Flask


app = Flask(__name__)

from app.views.home import home as home_blueprint
from app.views.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
