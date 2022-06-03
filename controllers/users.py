from flask import jsonify
from pipelines.aggregates import Aggregations
from db.mongoAcctions import MongoAccions
from utilities.utilities import Utilities
class Users:
    def getAllUsers(params):
        try:
            pipeline = Aggregations.getAllUsers(params['page'], params['limit'])
            data = MongoAccions.aggregate(collection='users', pipeline=pipeline)
            return jsonify({
                'error': False,
                'sucess': True,
                'data': data
            })
        except Exception as err:
            print(err)
            return jsonify({
                'error': True,
                'sucess': False,
                'data': []
            })
    def createUser(params):
        try:
            valName = Utilities.validateString(params['name'])
            valLastName = Utilities.validateString(params['last_name'])
            if not valLastName or not valName:
                    return jsonify({
                    'error': True,
                    'sucess': False,
                    'msg': 'error creating user missing or bad values',
                })
            else:
                valCreate = MongoAccions.createUser(valName, valLastName)
                if not valCreate:
                        return jsonify({
                        'error': True,
                        'sucess': False,
                        'msg': 'error creating user missing or bad values',
                    })
                else:
                    return jsonify({
                        'error': False,
                        'sucess': True,
                        'msg': 'user create successful'
                    })
        except Exception as err:
            print(err)
            return jsonify({
                'error': True,
                'sucess': False,
                'data': []
            })
    def modifyUser(params):
        try:
            id = params['id']
            if not id:
                return jsonify({
                    'error': True,
                    'sucess': False,
                    'msg': 'error creating user missing or bad values',
                })
            else:
                valName = Utilities.validateString(params['name'])
                valLastName = Utilities.validateString(params['last_name'])
                if not valLastName or not valName:
                        return jsonify({
                        'error': True,
                        'sucess': False,
                        'msg': 'error creating user missing or bad values',
                    })
                valModify = MongoAccions.modifyUser(valName, valLastName, params['id'])
                if valModify:
                    return jsonify({
                        'error': False,
                        'sucess': True,
                        'msg': 'user modify successful'
                    })
                else:
                    return jsonify({
                        'error': False,
                        'sucess': True,
                        'msg': 'user not found'
                    })
        except ValueError as err:
            print(err)
            return jsonify({
                'error': True,
                'sucess': False,
                'data': []
            })
    def deleteUser(id):
        try:
            if not id:
                return jsonify({
                    'error': True,
                    'sucess': False,
                    'msg': 'error delete user, missing or bad values',
                })
            else:
                valModify = MongoAccions.deleteUser(id)
                if valModify:
                    return jsonify({
                        'error': False,
                        'sucess': True,
                        'msg': 'user delete successful'
                    })
                else:
                    return jsonify({
                        'error': False,
                        'sucess': True,
                        'msg': 'user not found'
                    })
        except ValueError as err:
            print(err)
            return jsonify({
                'error': True,
                'sucess': False,
                'data': []
            })