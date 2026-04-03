### Book Log API
As someone who loves to read, I wanted to create a way to to track the books I've read while deepening my understanding of APIs. 
In this project, I created a RESTful API that serves as a book log to the user by implementing HTTP methods such as GET, DELETE, and POST.

## ⭐ Overview
# Tech Stack: Python, Flask, Postman
# Methods
1. get_books() - retrieve all books (GET)
2. get_book_by_id(book_id) - retreive book by index (GET)
3. get_book_by_title(book_title) - retrive book by title (GET)
4. get_book_by_author(book_author) - retrive book by author (GET)
5. add_book() - post book (POST)
6. delete_book_by_id(book_id) - delete book by id (DELETE)
7. delete_book_by_title(book_title) - delete book by title (DELETE)
8. delete_book_by_author(book_author) - delete book by author (DELETE)

## ⭐ API Endpoints
GET    /books                          - returns all books
GET    /books/<id>                     - returns a single book by id
GET    /books/title/<title>            - returns a single book by title
GET    /books/author/<author>          - returns all books by an author

POST   /books                          - adds a new book

DELETE /books/<id>                     - deletes a book by id
DELETE /books/title/<title>            - deletes a book by title
DELETE /books/author/<author>          - deletes all books by an author



