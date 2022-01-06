from flask import Flask, send_file
from flask_restful import Resource, Api, reqparse
from config import cfg
from icecream import ic


app = Flask(__name__)
api = Api(app)


class ParserApp(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str)
        parser.add_argument('width', type=str)
        parser.add_argument('save_links', type=str)

        url, width, save_links = parser.parse_args().values()
        return parser.parse_args()


class Test(Resource):
    def get(self):
        return send_file("static/file.txt")


api.add_resource(ParserApp, '/parser', endpoint='parser')
api.add_resource(Test, '/test', endpoint='test')


if __name__ == '__main__':
    app.run(debug=cfg.FLASK_DEBUG_MODE)
