from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Display TCP/IP Address</title>
</head>
<body>
    <h1>Your Public IP Address:</h1>
    <p id="ip">Loading...</p>

    <script>
        fetch('https://api.ipify.org?format=json')
            .then(response => response.json())
            .then(data => {
                document.getElementById('ip').textContent = data.ip;
            })
            .catch(error => {
                document.getElementById('ip').textContent = 'Unable to fetch IP address.';
                console.error('Error fetching IP:', error);
            });
    </script>
</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()