from flask import Flask, request, jsonify
from flask.ext import restful
from flask.ext.restful import reqparse
from acme_db import db
from acme_db import models


app = None


def create_app(conf):
    global app
    app = Flask(__name__)
    app.config.from_object(conf)
    api = restful.Api(app)
    api.add_resource(Aliens, '/v1/aliens')
    api.add_resource(ProbeReport, '/v1/report/')
    db.init(app.config['DB_URI'])

    return app


class Aliens(restful.Resource):
    def get(self):
        q = db.get_session().query
        parser = reqparse.RequestParser()
        parser.add_argument('start_id',
                            type=int,
                            default=0,
                            help='initial_id to get next page from')
        args = parser.parse_args()
        q = q(models.Alien).filter((id > args['start_id']))
        result = q.limit(app.config['QUERY_LIMIT']).all()

        result = [x.serialize() for x in result]
        result = jsonify(result=result)
        return result


class ProbeReport(restful.Resource):
    def get(self):
        q = db.get_session().query
        a = request.args # short name for the request argument dictionary
        result = []
        return result


if __name__ == '__main__':
    import config
    app = create_app(config)
    app.run(debug=True, port=9000)
