from flask import Flask
#Import the Plugin instance
from flask.ext.plugins import Plugin
#Import app which is initialized in pybossa.core
from flask import current_app as app

#This line is mandatory. 
#You can give any name to your template. 
#Recomended to give the same name as the name of the directory for your plugin.
__plugin__ = "TemplatePlugin"

#Version number for your template.
#This is optional
__version__ = "0.0.1"

#Create a class with the same name as specified in line 10
class TemplatePlugin(Plugin):
#The setup method is called when the plugin is setup by PyBossa
    def setup(self):
	#Import the blueprint defined in views.py
	from .views import blueprint
	#Register the blueprint with the PyBossa app instance. 
	#This will allow us to route to views within our plugin. 
	#The url_prefix parameter passed while registering denotes the prefix in the URL to route 	  views within this folder. 
	#You can give any prefix of your choice.
        app.register_blueprint(blueprint, url_prefix="/prefix")

#As in any flask application, we import views.py and models.py at the end to avoid circular imports
import views, models
