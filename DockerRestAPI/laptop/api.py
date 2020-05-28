# Laptop Service
from flask import Flask
import flask
from flask import request
from pymongo import MongoClient
import pymongo
from flask_restful import Resource, Api
import os

# Instantiate the app
app = Flask(__name__)
api = Api(app)
client = MongoClient("db", 27017)
db = client.tododb

class all_l(Resource):
    def get(self):
        top = request.args.get("top")

        if (top == None):
            top = 20

        _items = db.tododb.find().sort("Open", pymongo.ASCENDING).limit(int(top))
        items = [item for item in _items]
        return {
            'Open': [item['open_times'] for item in items],
            'Close': [item['close_times'] for item in items]
        }


class all_json(Resource):
    def get(self):
        top = request.args.get("top")
        if (top == None): top = 20

        _items = db.tododb.find().sort("Open", pymongo.ASCENDING).limit(int(top))
        items = [item for item in _items]
        return {
            'Open': [item['open_times'] for item in items],
            'Close': [item['close_times'] for item in items]
        }

class all_csv(Resource):
    def get(self):
        top = request.args.get("top")
        if (top == None): top = 20

        _items = db.tododb.find().sort("Open", pymongo.ASCENDING).limit(int(top))
        items = [item for item in _items]

        csv = ""
        for item in items:
            csv += item['open_times'] + ', ' + item['close_times'] + ', '

        return csv

class open_l(Resource):
    def get(self):
        top = request.args.get("top")
        if (top == None): top = 20

        _items = db.tododb.find().sort("Open", pymongo.ASCENDING).limit(int(top))

        return {
            'Open': [item['open_times'] for item in _items]
        }

class open_json(Resource):
    def get(self):
        top = request.args.get("top")
        if (top == None): top = 20

        _items = db.tododb.find().sort("Open", pymongo.ASCENDING).limit(int(top))
        
        return {
            'Open': [item['open_times'] for item in _items]
        }

class open_csv(Resource):
    def get(self):
        top = request.args.get("top")
        if (top == None): top = 20

        _items = db.tododb.find().sort("Open", pymongo.ASCENDING).limit(int(top))
        items = [item for item in _items]

        csv = ""
        for item in items:
            csv += item['open_times'] + ', '
        return csv

class close_l(Resource):
    def get(self):
        top = request.args.get("top")
        if (top == None): top = 20

        _items = db.tododb.find().sort("Close", pymongo.ASCENDING).limit(int(top))

        return {
            'Close': [item['close_times'] for item in _items]
        }

class close_json(Resource):
    def get(self):
        top = request.args.get("top")
        if (top == None): top = 20

        _items = db.tododb.find().sort("Close", pymongo.ASCENDING).limit(int(top))

        return {
            'Close': [item['close_times'] for item in _items]
        }

class close_csv(Resource):
    def get(self):
        top = request.args.get("top")
        if (top == None): top = 20

        _items = db.tododb.find().sort("Close", pymongo.ASCENDING).limit(int(top))
        items = [item for item in _items]


        csv = ""
        for item in items:
            csv += item['close_times'] + ', '
        return csv


api.add_resource(all_l, '/listAll')
api.add_resource(all_json, '/listAll/json')
api.add_resource(all_csv, '/listAll/csv')

api.add_resource(open_l, '/listOpenOnly')
api.add_resource(open_json, '/listOpenOnly/json')
api.add_resource(open_csv, '/listOpenOnly/csv')

api.add_resource(close_l, '/listCloseOnly')
api.add_resource(close_json, '/listCloseOnly/json')
api.add_resource(close_csv, '/listCloseOnly/csv')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
