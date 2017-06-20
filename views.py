from flask import render_template, session,flash
from flask import request, redirect, url_for
#Import Blueprint instance from flask
from flask import Blueprint

#Initialize the Blueprint instance for your plugin.
#The name of the templates folder has to be specified here.
#Else PyBossa searches for templates in the Core templates folder defined by PyBossa
blueprint = Blueprint('template', __name__, template_folder="templates")

#Use blueprint to route within your plugin
@blueprint.route('/')
@blueprint.route('/index')
def index():
    return render_template("index.html")
