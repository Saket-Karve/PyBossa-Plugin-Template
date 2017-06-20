from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.plugins import Plugin
from flask import current_app as app

__plugin__ = "Quiz"
__version__ = "0.0.1"

#app = Flask(__name__)
#app.config.from_object('config')
#db = SQLAlchemy(app)

#from flask import Blueprint
#blueprint = Blueprint('blueprint', __name__, template_folder="templates")



class Quiz(Plugin):
    def setup(self):
	from .views import blueprint
        app.register_blueprint(blueprint, url_prefix="/user_evaluation")


import views, models