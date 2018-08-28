<<<<<<< HEAD
from flask_restful import Resource
# Welcome
# displays welcome message


class Welcome(Resource):
    def get(self):
        return 'Hello world, this is our simple REST API Server!'
=======
from flask_restful import Resource
import Prometheus_client
import time


# Welcome
# displays welcome message


class Welcome(Resource):

    def get(self):
<<<<<<< HEAD
        #Prometheus_client.Metrics.inc_c()
        Prometheus_client.Metrics.c.labels('get', '/').inc()
        return 'Hello world, this is our simple REST API Server)'
>>>>>>> f_prometheus
=======
        Prometheus_client.Metrics.welcome_page_request.inc()
        return 'Hello world, this is our simple REST API Server!'
>>>>>>> f_prometheus
