from shared import db

class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(255),unique=True)
	age = db.Column(db.Integer)

	def __init__(self,username,age):
		self.username = username
		self.age = age

	def __repr__(self):
		return '<User %r>' % self.username 


if __name__ == '__main__':
	print User.query.all()
