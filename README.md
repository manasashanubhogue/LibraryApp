# LibraryApp

Application built as a part of Library Service, provides request/ endpoints for the users to perform following actions:
- User using email and title of book can request for the book, which inturn requests in creation of a book request and returns unique id - Form available to input data
- Using unique id, user can retreive request details - /request/<id>
- User can also view all requests present in the system - /request
- User can delete existing request- /request/<id>

Assumptions:
- No authentication/Authorization required to access above end points
- Not capable of handling high traffic/no concurrent writes


Dependencies:

python 3.9
Docker Engine, Docker compose


Installation guide

1. git clone
2. cd LibraryApp/
3. docker-compose build
4. docker-compose up

Outputs


Request Form : 
<img src="https://github.com/manasashanubhogue/LibraryApp/blob/main/app/static/Request%20Form.png" width="300" height="200">

All Requests:
<img src="https://github.com/manasashanubhogue/LibraryApp/blob/main/app/static/all_requests.png" width="500" height="250">

Particular Request:
<img src="https://github.com/manasashanubhogue/LibraryApp/blob/main/app/static/particular_request.png" width="300" height="150">
