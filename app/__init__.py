from flask import Flask
from flask_cors import CORS
import os
from os import environ 


app = Flask(__name__)
CORS(app)

from app import views

