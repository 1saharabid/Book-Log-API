from flask import Flask, jsonify, request

app = Flask(__name__)

#sample data
books = [
   {"id": 1, "title": "The Hunger Games", "author": "Suzanne Collins"},
   {"id": 2, "title": "Catching Fire", "author": "Suzanne Collins"},
   {"id": 3, "title": "Mockingjay", "author": "Suzanne Collins"}
]

#get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

#get book by id
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

#get book by title
@app.route('/books/title/<string:book_title>', methods=['GET'])
def get_book_by_title(book_title):
    for book in books:
        if book['title'] == book_title:
            return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books/author/<string:book_author>', methods=['GET'])
def get_book_by_author(book_author):
    lst_get = []
    for index, book in enumerate(books):
        if book['author'] == book_author:
            lst_get.append(book)
    if len(lst_get) == 0:
        return jsonify({'error': 'Author not found'}), 404
    else:
        return jsonify(lst_get)


#post a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_book['id'] = len(books) + 1
    books.append(new_book)
    return jsonify(new_book), 201

#delete by id
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book_by_id(book_id):
    for index, book in enumerate(books):
        if book['id'] == book_id:
            return jsonify(books.pop(index))
    return jsonify({'error': 'Book not found'}), 404

#delete by title
@app.route('/books/title/<string:book_title>', methods=['DELETE'])
def delete_book_by_title(book_title):
    for index, book in enumerate(books):
        if book['title'] == book_title:
            return jsonify(books.pop())
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books/author/<string:book_author>', methods=['DELETE'])
def delete_book_by_author(book_author):
    lst_delete = []
    for index, book in enumerate(books):
        if book['author'] == book_author:
            lst_delete.append(index)
    if len(lst_delete) == 0:
        return jsonify({'error': 'Author not found'}), 404
    else:
        for index in sorted(lst_delete, reverse=True):
            books.pop(index)
        return jsonify({'message': 'Titles removed!'})




            

if __name__ == '__main__':
    app.run(debug=True)