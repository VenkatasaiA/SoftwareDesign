import os
from .. import LOG


def init_app(app):
    global APP
    APP = app
    for folder in app.config["DIRECTORIES"]:
        if not os.path.exists(folder):
            os.mkdir(folder)
    LOG.info("Initialized application")
