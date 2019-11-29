from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:CHANGETHIS@35.246.48.37/card_game'
app.config['SECRET_KEY'] = 'CHANGE THIS'
db = SQLAlchemy(app)

from application import routes
