from flask_restful import Resource
import Prometheus_client
# Welcome
# displays welcome message


class Welcome(Resource):
    def get(self):
        Prometheus_client.Metrics.c.labels('get', '/').inc()
        return 'Hello world, this is our simple REST API Server!'

