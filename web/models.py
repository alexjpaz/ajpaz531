from google.appengine.ext import ndb
from google.appengine.ext import db

class Post(db.Expando):
	modified_date = db.DateProperty(auto_now=True)
	creation_date = db.DateProperty(auto_now_add=True)
	title = db.StringProperty()
	content = db.StringProperty()
	
class Max(db.Model):
	press = db.IntegerProperty()
	deadlift = db.IntegerProperty()
	bench = db.IntegerProperty()
	squat = db.IntegerProperty()
	date = db.DateProperty(auto_now_add=True)
	
class PersonalRecord(db.Model):
	weight = db.IntegerProperty()
	reps = db.IntegerProperty()
	lift = db.StringProperty()
	date = db.DateProperty(auto_now_add=True)