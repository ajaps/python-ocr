from flask import Flask, request
from flask_restful import reqparse, Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from scr.data import mongo_db
from scr.service.image_ocr import Image_Ocr
from scr.data.imports import File_Import
from scr.infrastructure.setup_elasticsearch import es

app = Flask(__name__)
api = Api(app)
app.elasticsearch = es if es else None

parser = reqparse.RequestParser()
parser.add_argument('image_url')
parser.add_argument('year')
parser.add_argument('month')
parser.add_argument('day')
parser.add_argument('page')

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
    def get(self):
        args = parser.parse_args()

        # If image url is empty
        if not args["image_url"]:
            return jsonify({'error': 'Source imagemust be specified'})
        if not args["page"]:
            return jsonify({'error': 'page number must be specified'})
        if not (args["year"] and args["month"] and args["day"]):
            return jsonify({'error': 'year, month and day must be specified'})

        try:
            paper_import = File_Import(page_number=args["page"], year=args["year"], month=args["month"], day=args["day"], file_url=args["image_url"])
            paper_import.save()
        except Exception as e:
            return {'error': str(e)}

        # Ocr_Engine = Image_Ocr(args["image_url"])
        # ocr_text = Ocr_Engine.get_text_and_positions()

        # newspaper = Paper(full_text=ocr_text['full_text'], page_number=args["page"], year=args["year"], month=args["month"], day=args["day"], **ocr_text['raw_data'])
        # newspaper.save()
 
        # try:
        #     paper_import = File_Import(page_number=args["page"], year=args["year"], month=args["month"], day=args["day"], file_url=args["image_url"])
        #     paper_import.save()
        # except Exception as e:
        #     return {'error': str(e)}

        date = str(paper_import.day) + '-' + str(paper_import.month) + '-' + str(paper_import.year)
        return jsonify({'date': date, 'page': paper_import.page_number, 'url': paper_import.file_url})

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

class Get_Record(Resource):
    def post(self):
        args = parser.parse_args()

        # If image url is empty
        if not args["image_url"]:
            return jsonify({'error': 'Source image must be specified'})

        frank = File_Import.objects(file_url=args["image_url"]).first()

        return jsonify(frank.paper.full_text)


api.add_resource(Tracks, '/tracks')  # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>')  # Route_3
api.add_resource(Ocr_Text, '/image/<file_name>')  # Route_3
api.add_resource(Return_Ocr_Text, '/ocr-image')  # Route_3 POST
api.add_resource(Return_hOcr, '/ocr-image')  # Route_3 GET - OCRing & Identifying page structure
api.add_resource(Ocr_Text_And_Position, '/text-and-position')  # Route_3 GET - OCRing & word postion on page
api.add_resource(Get_Record, '/get-record')  # Route_3 POST - Retrieve record

if __name__ == '__main__':
    app.run()

# Run app
# python ocr_api.py
