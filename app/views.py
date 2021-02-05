from flask import json, request, jsonify, render_template
from app import app
from app.forms import BookRequestForm, BookRequestSchema
from app.models import BookRequest
from app.utils import validate_and_get_booking_request

@app.route('/')
def home():
   form = BookRequestForm()
   return render_template('request_form.html', title='Request Book', form=form)

@app.route('/request', methods=['GET', 'POST'])
def handle_book_request():
   """ Method to handle book requests GET - to fetch all book requests made | POST - create a new book request """
   request_schema = BookRequestSchema()
   if request.method == "GET":
      # TODO: Ex- If user has been already notified, ignore those in list of requests, use below commented code
      # filter_param = {'notified_user': False}
      # book_req_obj.fetch_data_based_on_param(filter_param)
      book_req_obj = BookRequest()
      # get all book requests
      response_data = book_req_obj.fetch_all_data()
      result = [request_schema.dump(request_obj) for request_obj in response_data]
      return jsonify({"data": result}), 200
   if request.method == "POST":
      # validate the request from user
      has_error, data = validate_and_get_booking_request(request.form)
      if has_error:
         return jsonify({"error": data}), 400
      else:
         result = request_schema.dump(data)
         return jsonify({'data': result}), 200

@app.route('/request/<int:request_id>', methods=['GET', 'DELETE'])
def handle_book_request_by_id(request_id):
      pass