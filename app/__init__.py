from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import os


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:CostadoMarfimrx8*10@localhost:3306/storage.db'


app.config['SECRET_KEY'] = 'sucodeuva'

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload') # constante do endereço para armazenar a imagem


login_manager = LoginManager(app)
db = SQLAlchemy(app)