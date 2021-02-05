
import datetime
from app import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime


#TODO: Can be used for authentication and linked as fk to BookRequests
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Base(db.Model):
    __abstract__ = True
    created_date = db.Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.datetime.utcnow)

    def fetch_all_data(cls):
        """ Method returns all the data present in the table for the given model"""
        data = cls.query.all()
        return data

    def fetch_data_based_on_param(cls, filter_param):
        data = cls.query.filter_by(**filter_param).all()
        return data

class Book(Base):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    # author = db.Column(db.String())
    # publication = db.Column(db.String())


class BookRequest(Base):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    # time constraint - faced issue in fetching title,not much knowledge on how to back reference to get values
    # book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    # __table_args__ = (
    #     db.UniqueConstraint('book_id', 'user_email'),
    #   )
    # notified_user = db.Column(db.Boolean, default=False, nullable=False) #on notifying user, set to true
