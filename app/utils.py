from flask import request
from app import app
from app.database_utils import (
    book_exists, user_exists, book_request_exists, add_instance
) 
from app.forms import BookRequestForm
from app.models import Book, BookRequest, User


def validate_and_update_booking_request(form_data):
    # validate the request data using form validations
    has_error = False
    form = BookRequestForm()
    status_code = 200
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
            filter_param = {'title':title, 'user_email':email}
            book_request_obj = book_request_exists(filter_param)
            if book_request_obj:
                app.logger.info('Found an existing booking request')
                data = book_request_obj
            else:
                app.logger.info('Creating a new booking request')
                # create new request by user
                add_instance(BookRequest, **filter_param)
                # fetch newly created request data
                book_req_instance = BookRequest()
                data = book_req_instance.fetch_data_based_on_param(filter_param)[0]
                status_code = 201
        else:
            data = "Requested Book doesn't exist in the Library!"
            has_error = True
            status_code = 404
    else:
        data = form.errors
        has_error = True
        status_code = 400
    
    return has_error, data, status_code

def validate_and_get_booking_details(book_req_id):
    """ book_req_id: integer | Booking request id
    Method to validate the id requested and respond with booking request details"""
    has_error = False
    # if book exists, return title and other details, else throw error
    param = {'id':book_req_id}
    response_data = book_request_exists(param)
    if not response_data:
        response_data = "Requested Booking doesn't exist !"
        has_error = True
    return has_error, response_data