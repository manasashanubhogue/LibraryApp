from app.database_utils import (
    book_exists, user_exists, book_request_exists, add_instance, fetch_data_based_on_param
) 
from app.forms import BookRequestForm
from app.models import Book, BookRequest, User
from flask import request

def validate_and_get_booking_request(form_data):
    # validate the request data using form validations
    has_error = False
    form = BookRequestForm()
    if form.validate_on_submit():
        title = form_data.get('title')
        email = form_data.get('email')
        # verify if the book exists in db
        if book_exists(title):
            # check if user exists, if not create user
            # TODO: Not sure of the usecase of creation of user, creating new user as required
            # Posible usecase - relation b/w user and book request could be established as fk, and authenticate
            if not user_exists(email):
                add_instance(User, email=email)
            #Assumption: If request already exists, update timestamp-todo and return id
            book_request_obj = book_request_exists(title, email)
            if book_request_obj:
                data = book_request_obj    
            else:
                # create new request by user
                add_instance(BookRequest, user_email=email, title=title)
                # fetch newly created request data
                data = fetch_data_based_on_param(BookRequest, user_email=email, title=title)
            return has_error, data
        else:
            data = "Requested Book doesn't exist in the Library!"
            has_error = True
    else:
        data = form.errors
        has_error = True
    
    return has_error, data
