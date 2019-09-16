from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)


class Employees(Resource):
    def get(self):
        conn = db_connect.connect()  # connect to database
        # This line performs query and returns json result
        query = conn.execute("select * from employees")
        # Fetches first column that is Employee ID
        return {'employees': '[i[0] for i in query.cursor.fetchall()]'}


class Tracks(Resource):
    def get(self):
        # result = {'data': [dict(zip(tuple(query.keys()), i))
        #                    for i in query.cursor]}
        result = {
            'data': [
                {'name': 'Ajaps franklin'}
            ]
        }
        return jsonify(result)


class Employees_Name(Resource):
    def get(self, employee_id):
        result = {
            'data': [
                 {'name': 'Ajaps franklin'}
            ]
        }
        return jsonify(result)


api.add_resource(Employees, '/employees')  # Route_1
api.add_resource(Tracks, '/tracks')  # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>')  # Route_3


if __name__ == '__main__':
    app.run(port='5002')

# Run app
# python ocr_api.py
