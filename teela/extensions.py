from flask_cache import Cache
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


cache = Cache()
db = SQLAlchemy()
login_manager = LoginManager()
