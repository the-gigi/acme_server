from flask import Flask, request
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)


class Aliens(restful.Resource):
    def get(self):
        a = request.args # short name for the request argument dictionary
        result = []
        return result


class ProbeReport(restful.Resource):
    def get(self):
        a = request.args # short name for the request argument dictionary
        result = []
        return result


api.add_resource(Aliens, '/v1/aliens')
api.add_resource(ProbeReport, '/v1/report/')


if __name__ == '__main__':
    app.run(debug=True, port=9000)
