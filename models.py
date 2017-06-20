#Import the db instance from pybossa.core to get access to the PyBossa Database
from pybossa.core import db

#Define your models as classes in the same way it is done for any flask application
class Sample(db.Model):
	field1 = db.Column(db.String)
	field2 = db.Column(db.Integer)
