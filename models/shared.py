import sys
sys.path.append('/home/trevor/web')
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalch.testapp import app
db = SQLAlchemy(app)
