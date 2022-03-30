""" import os
import connexion
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
USERNAME ='postgres'
PASSWORD ="canada12"
PUBLIC_IP_ADDRESS ="127.0.0.1"
DBNAME ="postgres"
PROJECT_ID ="cnprojext"
INSTANCE_NAME ="cn-projecto"

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)
#Line 9 uses the basedir variable to create the Connexion app instance and give it the path to the swagger.yml file.

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{0}:{1}@{2}/{3}".format(USERNAME, 
        PASSWORD,
        PUBLIC_IP_ADDRESS, DBNAME)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

print("---------",type(app))
# Create the SQLAlchemy db instance
db = SQLAlchemy(app) #--> here """