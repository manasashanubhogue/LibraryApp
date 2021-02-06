import json
import unittest, datetime
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from app.models import User, BookRequest, Book


class TestRequestBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['TESTING'] = True
        cls.app_obj = app

    def setUp(self):
        with self.app_obj.app_context():
            self.app = current_app.test_client()
            # self.db.drop_all()
            db.create_all()
            book_obj=Book(title="Test Book")
            book_req_obj1=BookRequest(title="Test Book", user_email="abcd1@gmail.com")
            book_req_obj2=BookRequest(title="Test Book", user_email="abcd2@gmail.com")
            db.session.add(book_obj)
            db.session.add(book_req_obj1)
            db.session.add(book_req_obj2)
            db.session.commit()

    def tearDown(self):
        with self.app_obj.app_context():
            db.drop_all()

    def test_home_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def create_book_request(self):
        input_data = {"email": 'abc@gmail.com', "title": "Test Book"}
        response = self.app.post('/request', data=input_data, content_type='multipart/form-data')
        return response

    def test_book_request_creation(self):
        # creating request with valid data
        response = self.create_book_request()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['data']['title'], "Test Book")

    def test_request_creation_incorrect_title(self):
        # creating request with book that does not exists in db
        input_data = {"email": 'abc@gmail.com', "title": "Test Book1"}
        response = self.app.post('/request', data=input_data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data)['error'], "Requested Book doesn't exist in the Library!")

    def test_request_creation_invalid_email(self):
        # creating request with incorrect email
        input_data = {"email": 'abc', "title": "Test Book1"}
        response = self.app.post('/request', data=input_data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)['error']['email'],  ['Invalid email address.'])

    def test_fetching_all_requests(self):
        # creating request with incorrect email
        response = self.app.get('/request')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len((json.loads(response.data)['data'])),  2)

    def test_fetch_particular_request(self):
        book_req_response = self.create_book_request()
        request_id = json.loads(book_req_response.data)['data']['id']
        response = self.app.get('/request/{}'.format(request_id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['data']['title'], "Test Book")

    def test_fetchbooking_invalid_request_id(self):
        response = self.app.get('/request/100')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)['error'], "Requested Booking doesn't exist !")

    def test_delete_request_by_valid_id(self):
        book_req_response = self.create_book_request()
        request_id = json.loads(book_req_response.data)['data']['id']
        response = self.app.delete('/request/{}'.format(request_id))
        self.assertEqual(response.status_code, 200)

    def test_delete_request_by_invalid_id(self):
        response = self.app.delete('/request/100')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)['error'], "Requested Booking doesn't exist !")
