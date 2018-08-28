from prometheus_client import start_http_server, Summary, Counter
class Metrics:
    c = Counter('ID_request', 'HTTP', ['method', 'endpoint'])
    b = Counter('ID_not_found', 'Error 404')
    @staticmethod
    # Start up the server to expose the metrics.
    def start():
        start_http_server(8000)
