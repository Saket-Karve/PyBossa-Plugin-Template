# PyBossa-Plugin-Template
Template for adding plugins to PyBossa

Plugins are an integral part of the PyBossa environment. They help you add new features to the existing PyBossa implementation without having to modify the core code. Plugins help improve the Crowdsourcing application to suit your specific requirements along with using PyBossa as a base.

It is very easy to add plugins to your PyBossa application. Just include the __init__.py and info.json as in this template to make your plugin running within the installed PyBossa instance.

Plugins can also include other flask files like views, models and forms.

Simply add the required views, models and forms like in any flask application with minor changes in some files as specified in this template.

## To add your models to the PyBossa database, run the following python script

`python cli.py create_db`


