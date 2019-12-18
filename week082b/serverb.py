from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='../')


acts=[
  { "name":"joe", "id":1,"totalVotes":4},
  { "name":"mary", "id":2, "totalVotes":5},
  { "name":"brid", "id":3, "totalVotes":6}
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

#curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X POST -d '{"name":"Jeremy"}' http://127.0.0.1:5000/acts
@app.route('/acts', methods=['POST'])
def create():
  global nextId
  if not request.json:
    abort(400)
  # other checking that properly formatted
  act = {
      "id":nextId,
      "name":request.json['name'],
      "totalVotes":0
      }
  nextId += 1
  acts.append(act)
  return jsonify(act)

#curl  -X DELETE http://127.0.0.1:5000/acts/1
@app.route('/acts/<int:id>', methods=['DELETE'])
def delete(id):
  foundActs = list(filter(lambda a: a['id']== id, acts))
  if (len(foundActs) == 0):
    abort(404)
  acts.remove(foundActs[0])
  return jsonify({"deleted successfully":True})

#curl -i -H "Content-Type: application/json"  -d '{"votes":5}' http://127.0.0.1:5000/votes/1
@app.route('/votes/<int:actId>', methods=['POST'])
def addVote(actId):
  foundActs = list(filter(lambda a : a['id']==actId, acts))
  if len(foundActs)==0:
    abort(404)
  if not request.json:
    abort(400)
  if not 'votes' in request.json or type(request.json['votes']) is not int:
    abort(401)
  newVote = request.json['votes']
  foundActs[0]['totalVotes'] += newVote
  return jsonify(foundActs[0])

@app.route('/votes/leaderboard')
def getleaderBoard():
  acts.sort(key=lambda x: x['totalVotes'], reverse=True)
  return jsonify(acts)

if __name__ == '__main__' :
    app.run(debug= True)
