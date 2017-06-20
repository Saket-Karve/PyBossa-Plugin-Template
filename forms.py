#There are no changes required in this file. 
#Create forms as usual for any general flask application
from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms import validators, ValidationError

#Declare a class for adding a form to the plugin as in any flask application
class sampleForm(Form):
	field1 = StringField('field1', [validators.Required("Field Required")])
	field2 = TextAreaField('field2')

