import unittest
import os
#import coverage

#from flask_script import Manager
from flask.ext.script import Manager

from portal import APP as app
from portal.models import db

manager = Manager(app)

if __name__ == '__main__':
    manager.run()