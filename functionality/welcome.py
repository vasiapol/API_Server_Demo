from flask_restful import Resource
import Prometheus_client
import time

# Welcome
# displays welcome message


class Welcome(Resource):
    @REQUEST_TIME.time()
    def get(self):
        Prometheus_client.Metrics.c.labels('get', '/').inc()
        return 'Hello world, this is our simple REST API Server)'
