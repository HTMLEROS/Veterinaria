from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg://usuario:contraseña@localhost/nombre_bd"
app.config['SQLALCHEMY_DATABASE_URI'] = "htmleros+psycopg://htmleros:1234@localhost/vetcontrol"
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
from routes import *