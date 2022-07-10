import os
from portal import LOG


def init_app(app):
    global APP
    APP = app
    for folder in app.config["DIRECTORIES"]:
        if not os.path.exists(folder):
            print('yes')
            os.mkdir(folder)
    # Talisman(app)
    LOG.info("Initialized application")
