from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models so they are registered with SQLAlchemy
from .users import Users
from .preferences import Preferences
