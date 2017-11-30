from flask import Flask
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser

from control import floor

app = Flask(__name__)
api = Api(app)


class HeatFloor(Resource):
    @staticmethod
    def get():
        return {'isOn': floor.is_on()}

    @staticmethod
    def put():
        parser = RequestParser(bundle_errors=True)
        parser.add_argument('isOn', required=True, type=bool, location='json')
        args = parser.parse_args()

        if args['isOn']:
            floor.switch_on()
        else:
            floor.switch_off()


api.add_resource(HeatFloor, '/api/heatfloor')
if __name__ == '__main__':
    app.run(host='0.0.0.0')
