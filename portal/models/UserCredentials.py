from . import db
from datetime import datetime
from sqlalchemy import Sequence


class UserCredentials(db.Model):
    __bind_key__ = 'db'
    Id = db.Column(db.Integer,Sequence('user_seq',start=1), unique=True, nullable=False, primary_key=True)
    user_uid=db.Column(db.String(255))
    password = db.Column(db.String(255))
    username = db.Column(db.String(255),nullable=False)
    email_id = db.Column(db.String(255))
    active=db.Column(db.String(255))
    status = db.Column(db.String(255), nullable=False)
    user_created_time = db.Column(db.TIMESTAMP, default=datetime.now, nullable=False)
    created_by = db.Column(db.String(255))
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
