from app import db
from app.models import Book, BookRequest, User

# create data
# def create_books():
#     book1 = Book(title='Flask Web Dev 2e')
#     book2 = Book(title='The New And Improved Flask Mega')
#     book3 = Book(title='Complete Web Application')
#     db.session.add(book1)
#     db.session.add(book2)
#     db.session.add(book3)
#     db.session.commit()

def book_exists(title):
    # mehtod to check if title exists in the table
    return Book.query.filter_by(title=title).first()

def user_exists(email):
    # mehtod to check if user email exists in the table
    return User.query.filter_by(email=email).first()

def book_request_exists(filter_param):
    """
    filter_param - model accepted filters
    format - (id=some_id, email=email, ..)
    """
    # verify is request has alreayd been made by user for given book
    return BookRequest.query.filter_by(**filter_param).first()

def add_instance(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    commit_changes()

def commit_changes():
    db.session.commit()

def delete_instance(model, id):
    model.query.filter_by(id=id).delete()
    commit_changes()