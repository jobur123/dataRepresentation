from flask import Flask, jsonify, request, abort
from zbookDAO import bookDAO

app = Flask(__name__, static_url_path='', static_folder='../')



# books=[
#   { "id":1, "Title":"Harry Potter", "Author":"JK", "price":1000},
#   { "id":2, "Title":"The Snapper", "Author":"Roddy Doyle", "price":800},
#   { "id":3, "Title":"The Bible", "Author":"John", "price":1500}
# ]
# nextId=4

#curl "http://127.0.0.1:5000/books"
@app.route('/books')
def getAll():
  results = bookDAO.getAll()
  return jsonify(results)

#curl "http://127.0.0.1:5000/books/2"
@app.route('/books/<int:id>')
def findById(id):
  foundBook = bookDAO.findByID(id)
  return jsonify(foundBook)

#curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X POST -d '{"Title":"War","Author":"James P","Price":35}' http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
  #global nextId
  if not request.json:
    abort(400)
  # other checking that properly formatted
  book = {
      #"id": nextId,
      "Title": request.json['Title'],
      "Author": request.json['Author'],
      "Price": request.json['Price']
  }
  values =(book['Title'],book['Author'],book['Price'])
  newId = bookDAO.create(values)
  book['id'] = newId
  return jsonify(book)

#curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X PUT -d '{"id":3,"Title":"War","Author":"James B","price":350}' http://127.0.0.1:5000/books/3
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
  foundBook = bookDAO.findByID(id)
  if not foundBook:
    abort(404)
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
  values = (foundBook['Title'], foundBook['Author'], foundBook['price'], foundBook['id'])
  bookDAO.update(values)
  return jsonify(foundBook)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
  bookDAO.delete(id)
  return jsonify({"deleted successfully":True})



if __name__ == '__main__' :
    app.run(debug= True)
