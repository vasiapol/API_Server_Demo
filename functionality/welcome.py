from flask_restful import Resource
import Prometheus_client
import time


# Welcome
# displays welcome message


class Welcome(Resource):

    def get(self):
        Prometheus_client.Metrics.welcome_page_request.inc()
        html_str="""<html>
<header><title>This is title</title></header>
<body>
Hello world
</body>
</html>"""
        # return 'Hello world, this is our simple REST API Server!'
         return html_str
