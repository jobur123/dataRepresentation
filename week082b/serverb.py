from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='../')


acts=[
  { "name":"joe", "id":1},
  { "name":"mary", "id":2},
  { "name":"brid", "id":3}
]
nextId=4

#curl "http://127.0.0.1:5000/acts"
@app.route('/acts')
def getAll():
  return jsonify(acts)

#curl "http://127.0.0.1:5000/acts/2"
@app.route('/acts/<int:id>')
def findById(id):
  foundActs = list(filter(lambda a : a['id'] == id, acts))
  if len(foundActs) == 0:
    return jsonify({}), 204
  return jsonify(foundActs[0])

#curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X POST -d '{"Title":"War","Author":"James P","price":350}' http://127.0.0.1:5000/books
@app.route('/acts', methods=['POST'])
def create():
  global nextId
  if not request.json:
    abort(400)
  # other checking that properly formatted
  act = {
      "id":nextId,
      "name":request.json['name']
  }
  nextId +=1
  acts.append(act)
  return jsonify(act)

@app.route('/acts/<int:id>', methods=['DELETE'])
def delete(id):
  foundActs = list(filter(lambda a: a['id']== id, acts))
  if (len(foundActs) == 0):
    abort(404)
  acts.remove(foundActs[0])
  return jsonify({"deleted successfully":True})

@app.route('/acts/<int:actId>', methods=['POST'])
def addVote(actId):
  return "in add Vote for act ", +str(actId)

@app.route('/acts/leaderboard', methods=['POST'])
def getleaderBoard(actId):
  return "in add Vote for act ", +str(actId)


if __name__ == '__main__' :
    app.run(debug= True)
