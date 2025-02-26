import socket

from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread


class _RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.send_header("Content-Length", 0)

    def do_PUT(self):
        self.send_response(200)
        self.send_header("Content-Length", 0)
        self.end_headers()
        self.server.put_requests += 1

    def log_request(self, code='-', size='-'):
        pass


class HTTPServerWithCounter(HTTPServer):
    def __init__(self, *args, **kwargs):
        super(HTTPServerWithCounter, self).__init__(*args, **kwargs)
        self.put_requests = 0


class MockHTTPServer(object):

    def __init__(self):
        self._port = -1
        self._server = None
        self._thread = None

    def get_free_port(self):
        s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
        s.bind(('localhost', 0))
        _address, port = s.getsockname()
        s.close()

        self._port = port
        return port

    def start(self):
        self._server = HTTPServerWithCounter(('localhost', self._port), _RequestHandler)

        self._thread = Thread(target=self._server.serve_forever)
        self._thread.daemon = True
        self._thread.start()

    def shutdown(self):
        self._server.shutdown()

    def get_number_of_put_requests(self):
        result = self._server.put_requests
        self._server.put_requests = 0
        return result
