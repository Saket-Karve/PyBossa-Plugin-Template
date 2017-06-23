# PyBossa Plugin Template

Template for adding plugins to PyBossa

Plugins are an integral part of the PyBossa environment. They help you add new features to the existing PyBossa implementation without having to modify the core code. Plugins help improve the Crowdsourcing application to suit your specific requirements along with using PyBossa as a base.

It is very easy to add plugins to your PyBossa application. Just include the __init__.py and info.json as in this template to make your plugin running within the installed PyBossa instance.

Plugins can also include other flask files like views, models and forms.

Simply add the required views, models and forms like in any flask application with minor changes in some files as specified in this template.

## Add your models to the PyBossa database

Run the following python script

`python cli.py create_db`

After adding your tables to the database, run the server using

`python run.py`

Note: The current version of PyBossa is not able to rebuild the database. The drop tables command produces errors when you have ForeignKeyConstraint between tables. Hence, you will have to delete all tables using DROP ... CASCADE before adding your tables to the database. You can use PgAdmin III to manage your database with the help of GUI.


