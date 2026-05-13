import http.server
import ssl
import subprocess
import threading
import time
import socket

# Configuration
HTTPS_PORT = 443
HTTP_PORT = 8000
CERT_FILE = 'C:\\Users\\snowm\\cert.crt'
KEY_FILE = 'C:\\Users\\snowm\\cert.key'

def run_django():
    subprocess.run(['.\\venv\\Scripts\\python.exe', 'manage.py', 'runserver', str(HTTP_PORT)])

# Start Django in a separate thread
threading.Thread(target=run_django, daemon=True).start()
time.sleep(3) # Wait for Django to start

# Simple Proxy Logic
class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Redirect all requests to localhost:8000
        self.send_response(302)
        self.send_header('Location', f'http://localhost:{HTTP_PORT}{self.path}')
        self.end_headers()

# Server Setup
httpd = http.server.HTTPServer(('0.0.0.0', HTTPS_PORT), ProxyHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile=CERT_FILE, keyfile=KEY_FILE, server_side=True)

print(f"Serving HTTPS on https://localhost:{HTTPS_PORT}")
httpd.serve_forever()
