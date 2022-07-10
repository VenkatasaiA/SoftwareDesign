from datetime import datetime

from . import db


class FuelQuote(db.Model):
    __bind_key__ = 'db'
    fuel_quote_id = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    user_id = db.Column(db.String(255))
    quantity = db.Column(db.String(255))
    cur_gallon_price = db.Column(db.String(255))
    total_price = db.Column(db.String(255))
    state = db.Column(db.String(255))
    country = db.Column(db.String(255))
    address = db.Column(db.String(2000))
    phone_number = db.Column(db.String(255))
    fuel_type=db.Column(db.String(255))
    cur_gst=db.Column(db.String(255))
    is_state=db.Column(db.String(255))
    status=db.Column(db.String(255))
    created_date = db.Column(db.TIMESTAMP, default=datetime.now)
    delivery_date = db.Column(db.TIMESTAMP)
    updated_date = db.Column(db.TIMESTAMP, default=datetime.now)
    attributes_1 = db.Column(db.String(255))
    attributes_2 = db.Column(db.String(255))
    attributes_3 = db.Column(db.String(255))
    attributes_4 = db.Column(db.String(255))
    attributes_5 = db.Column(db.String(255))
    attributes_6 = db.Column(db.String(255))
    attributes_7 = db.Column(db.String(255))
    attributes_8 = db.Column(db.String(255))
    attributes_9 = db.Column(db.String(255))
    attributes_10 = db.Column(db.String(255))
    attributes_11 = db.Column(db.String(255))
    attributes_12 = db.Column(db.String(255))
    attributes_13 = db.Column(db.String(255))
    attributes_14 = db.Column(db.String(255))
    attributes_15 = db.Column(db.String(255))
    attributes_16 = db.Column(db.String(255))
    attributes_17 = db.Column(db.String(255))
    attributes_18 = db.Column(db.String(255))
    attributes_19 = db.Column(db.String(255))
    attributes_20 = db.Column(db.String(255))
