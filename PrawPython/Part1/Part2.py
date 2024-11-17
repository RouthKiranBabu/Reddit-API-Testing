import http.server
import socketserver
import json

# Specify the port number
PORT = 8000

class JSONHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':  # Define a route for the JSON
            # Read the JSON file
            with open('data.json', 'r') as file:
                data = json.load(file)
            
            # Set HTTP headers
            self.send_response(200)  # OK status
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            # Write JSON data as response
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            # Handle other paths
            self.send_response(404)  # Not Found status
            self.end_headers()
            self.wfile.write(b'Not Found')

# Create and start the server
with socketserver.TCPServer(("", PORT), JSONHandler) as httpd:
    print(f"Serving JSON on localhost:{PORT}. Access it at http://localhost:{PORT}/data")
    httpd.serve_forever()
