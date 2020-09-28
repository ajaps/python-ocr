from flask import Flask, request
from flask_restful import reqparse, Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from get_image_text import Image_Ocr

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('image_url')


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


class Ocr_Text(Resource):
    def get(self, file_name):
        p = Image_Ocr(file_name)
        ocr_text = p.get_text_from_image()

        result = {
            'data': ocr_text
        }

        return jsonify(result)

class Ocr_Text_And_Position(Resource):
    def get(self, file_name):
        p = Image_Ocr(file_name)
        ocr_text_position = p.get_text_and_positions()

        result = {
            'data': ocr_text_position
        }

        return jsonify(result)


class Return_Ocr_Text(Resource):
    def post(self):
        args = parser.parse_args()

        # If image url is empty
        if not args["image_url"]:
            return jsonify({'error': 'Source image must be specified'})

        Ocr_Engine = Image_Ocr(args["image_url"])
        ocr_text = Ocr_Engine.get_text_from_image()

        return jsonify(ocr_text)

class Return_hOcr(Resource):
    def get(self):
        args = parser.parse_args()

        # If image url is empty
        if not args["image_url"]:
            return jsonify({'error': 'Source image must be specified'})

        Ocr_Engine = Image_Ocr(args["image_url"])
        ocr_text = Ocr_Engine.get_hOCR()

        return jsonify(ocr_text)


api.add_resource(Tracks, '/tracks')  # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>')  # Route_3
api.add_resource(Ocr_Text, '/image/<file_name>')  # Route_3
api.add_resource(Return_Ocr_Text, '/ocr-image')  # Route_3 POST
api.add_resource(Return_hOcr, '/ocr-image')  # Route_3 GET - OCRing & Identifying page structure
api.add_resource(Ocr_Text_And_Position, '/text-and-position')  # Route_3 GET - OCRing & word postion on page

if __name__ == '__main__':
    app.run()

# Run app
# python ocr_api.py
