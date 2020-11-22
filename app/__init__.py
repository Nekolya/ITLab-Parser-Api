from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from os import environ 
from sqlalchemy import Table, Column, Integer, String, ForeignKey


app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///" + os.path.join(basedir, 'output/table.db')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models

