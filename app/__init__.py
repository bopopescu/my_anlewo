from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import pymysql

pymysql.install_as_MySQLdb()
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app, use_native_unicode='utf8')
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)
moment = Moment(app)

from app import routes, models, error
