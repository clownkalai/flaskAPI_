import sys

# add your project directory to the sys.path
project_home = '/opt/render/project/src/'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from src import run as application  # noqa
