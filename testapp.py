from flask import Flask
from werkzeug.wrappers import Request,Response
from werkzeug.serving import run_simple
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:kfelagund7@173.220.194.84/mediasrv'
app.debug = True

from models.user import User

@app.route('/')
def root():
	usrs = User.query.all()
	
	return Response([json.dumps([u.username for u in usrs ])], mimetype='application/json')


if __name__ == '__main__':
	run_simple('localhost',5000,app,use_debugger=True,use_reloader=True)
