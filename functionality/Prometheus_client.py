from prometheus_client import start_http_server, Summary, Counter
class Metrics:
    request_by_id = Counter('ID_request', 'HTTP', ['method', 'endpoint'])
    welcome_page_request= Counter('welcome_page_request', 'Counts number of requests')
    bad_request = Counter('ID_not_found', 'HTTP', ['method', 'endpoint'])
    select_all_id = Summary('request_processing_seconds', 'Time spent processing request')
    @staticmethod
    # Start up the server to expose the metrics.
    def start():
        start_http_server(8000)
