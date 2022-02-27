from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import (
    JWTManager
)
import datetime
from const import *

database_file = "sqlite:///Database.db"

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = SECRET_KEY  # Change this!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=120)
jwt = JWTManager(app)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from main import *
if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8000, debug=True)