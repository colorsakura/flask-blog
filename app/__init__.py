# coding:utf-8
import os
from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):

	app = Flask(__name__)
	app.config.from_object(config[config_name])

	db.init_app(app)

	from app.views.home import home as home_blueprint
	from app.views.admin import admin as admin_blueprint
	from app.api import api as api_blueprint

	app.register_blueprint(home_blueprint)
	app.register_blueprint(admin_blueprint, url_prefix="/admin")
	app.register_blueprint(api_blueprint, url_prefix="/api")

	return app