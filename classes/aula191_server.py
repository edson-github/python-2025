from http.server import HTTPServer, SimpleHTTPRequestHandler
import json

class RequestHandler(SimpleHTTPRequestHandler):
    """"
    Simple HTTP request handler with a custom GET method.\n
    This handler responds to GET requests with a JSON object containing a message and a status.\n
    """
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response_data = {
            'message': 'Hello from the test server!',
            'status': 'success'
        }
        
        self.wfile.write(json.dumps(response_data).encode())

def run_server(port=3333):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()