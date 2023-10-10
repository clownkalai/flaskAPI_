import sys

# add your project directory to the sys.path
project_home = '/opt/render/project/src/'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
#from run import app as application  # noqa
from flaskAPI_JWT import run  # Replace 'your_app' with the actual name of your Flask application module

application = app
