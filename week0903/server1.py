from flask import Flask, jsonify, request, abort


app = Flask(__name__, static_url_path='', static_folder='../')



books=[
  { "id":1, "Title":"Harry Potter", "Author":"JK", "price":1000},
  { "id":2, "Title":"The Snapper", "Author":"Roddy Doyle", "price":800},
  { "id":3, "Title":"The Bible", "Author":"John", "price":1500}
]
nextId=4

#curl "http://127.0.0.1:5000/books"
@app.route('/books')
def getAll():
  return jsonify(books)

#curl "http://127.0.0.1:5000/books/2"
@app.route('/books/<int:id>')
def findById(id):
  foundBooks = list(filter(lambda b : b['id'] == id, books))
  if len(foundBooks) == 0:
    return jsonify({}), 204
  return jsonify(foundBooks[0])

#curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X POST -d '{"Title":"War","Author":"James P","price":350}' http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
  global nextId
  if not request.json:
    abort(400)
  # other checking that properly formatted
  book = {
      "id": nextId,
      "Title": request.json['Title'],
      "Author": request.json['Author'],
      "price": request.json['price']
  }
  nextId +=1
  books.append(book)
  return jsonify(book)

#curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X PUT -d '{"id":3,"Title":"War","Author":"James B","price":350}' http://127.0.0.1:5000/books/3
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
  foundBooks = list(filter(lambda b: b['id']== id, books))
  if (len(foundBooks) == 0):
    abort(404)
  foundBook = foundBooks[0]
  if not request.json:
    abort(400)
  reqJson = request.json
  if 'price' in reqJson and type(reqJson['price']) is not int:
    abort(400)
  if 'Title' in reqJson:
    foundBook['Title']= reqJson['Title']
  if 'Author' in reqJson:
    foundBook['Author']= reqJson['Author']
  if 'price' in reqJson:
    foundBook['price']= reqJson['price']
  return jsonify(foundBook)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
  foundBooks = list(filter(lambda b: b['id']== id, books))
  if (len(foundBooks) == 0):
    abort(404)
  books.remove(foundBooks[0])
  return jsonify({"deleted successfully":True})



if __name__ == '__main__' :
    app.run(debug= True)
