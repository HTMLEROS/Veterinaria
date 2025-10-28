from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://usuario:contraseña@localhost/vetcontrol'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
from routes import *