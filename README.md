# LibraryApp

Application built as a part of Library Service, provides request/ endpoints for the users to perform following actions:
- User using email and title of book can request for the book, which inturn requests in creation of a book request and returns unique id
- Using unique id, user can retreive request details
- User can also view all requests present in the system
- User can delete existing request

Assumptions:
- No authentication/Authorization required to access above end points


Dependencies:

python 3.9
Docker Engine, Docker compose


Installation guide

1. git clone
2. cd LibraryApp/
3. docker-compose build
4. docker-compose up
