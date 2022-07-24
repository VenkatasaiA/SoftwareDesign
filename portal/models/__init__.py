from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(
    engine_options={'connect_args': {'connect_timeout': 2000}}
)


def init_app(app):
    db_connection_string = app.config["DB_CONNECTION_STRING"]
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_BINDS'] = {
        'db': db_connection_string
    }
    db.init_app(app)
    app.logger.info('Initialized models')
    with app.app_context():
        from .ClientInformation import ClientInformation
        from .price_management import PriceManagement
        from .UserCredentials import UserCredentials
        from .FuelQuote import FuelQuote
        db.create_all(bind=['db'])
        db.session.commit()
        app.logger.debug('All tables are created')
