from flask import Flask
from flask_cors import CORS
from config import SECRET_KEY

app = Flask(__name__)

CORS(app)

app.config['SECRET_KEY'] = SECRET_KEY

from app import views