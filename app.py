
from flask import request, jsonify, Response, Flask
from controllers.users import Users

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return Response("Not found", status=404, mimetype="application/json")

@app.route('/getUsers', methods=['GET'])
def getAllUsers():
    try:
        page = request.args.get('page', default=10, type=int)
        rows = request.args.get('limit', default=10, type=int)
        params = {'page': page, 'limit': rows}
        res = Users.getAllUsers(params)
        return res
    except Exception as err:
        return jsonify({
            'error': True,
            'sucess': False,
            'data': []
        })
@app.route('/createUser', methods=['POST'])
def createUser():
    try:
        res = Users.createUser(request.json)
        return res
    except Exception as err:
        print(err)
        return jsonify({
            'error': True,
            'sucess': False,
            'data': []
        })

@app.route('/modifyUser', methods=['PATCH'])
def modifyUser():
    try:
        res = Users.modifyUser(request.json)
        return res
    except Exception as err:
        print(err)
        return jsonify({
            'error': True,
            'sucess': False,
            'data': []
        })

@app.route('/deleteUser', methods=['DELETE'])
def deleteUSer():
    try:
        id = request.args.get('id')
        res = Users.deleteUser(id)
        return res
    except Exception as err:
        return jsonify({
            'error': True,
            'sucess': False,
            'data': []
        })


if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=5000, ssl_context='adhoc')
    app.run(debug=True, host='0.0.0.0', port=5000)