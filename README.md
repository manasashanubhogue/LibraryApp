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
curl --location --request POST 'http://localhost:5000/request' \
--form 'email="abx@gmail.com"' \
--form 'title="Complete Web Application"'

<img src="https://github.com/manasashanubhogue/LibraryApp/blob/main/app/static/Request%20Form.png" width="300" height="200">

All Requests: curl --location --request GET 'http://localhost:5000/request'

<img src="https://github.com/manasashanubhogue/LibraryApp/blob/main/app/static/all_requests.png" width="500" height="250">

Particular Request: curl --location --request GET 'http://localhost:5000/request/1'
<img src="https://github.com/manasashanubhogue/LibraryApp/blob/main/app/static/particular_request.png" width="300" height="150">

Delete Request: curl --location --request DELETE 'http://localhost:5000/request/4'


TestCases:
```docker exec -it libraryapp_web_1 bash```
```python -m unittest```