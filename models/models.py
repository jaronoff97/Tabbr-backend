from app import db
from sqlalchemy.dialects.postgresql import JSON


class BaseModel():

    def __repr__(self):
        try:
            return '<{0} {1}>'.format(self.__class__.__name__, self.id)
        except AttributeError:
            return '<{0}>'.format(self.__class__.__name__)


class Account(db.Model, BaseModel):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String())
    users = db.relationship('User',
                            backref='accounts',
                            lazy='dynamic')

    def __init__(self, account_name):
        self.account_name = account_name


class User(db.Model, BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String())
    account_holder_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))

    def __init__(self, user_name):
        self.user_name = user_name
