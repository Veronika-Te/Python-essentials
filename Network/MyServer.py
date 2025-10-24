from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests"""
        try:
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'GET request received!')
        except Exception as e:
            self.send_response(500)  # Server error
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(f'Server Error: {str(e)}'.encode())
        
    def do_POST(self):
        """Handle POST requests"""
        try:
            content_length = int(self.headers['Content-Length'])#,64)
            post_data = self.rfile.read(content_length) 
            print(f"Received POST data: {post_data}")
            try:
                # Example file path 
                file_path = "user_data.json"
                # Reading the existing data from the file (if it exists)
                with open(file_path, "r") as f:
                     data = json.load(f)

                # Respond with the updated data
                self.send_response(201)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {"message": "Data successfully added", "data": data}
                
                self.wfile.write(json.dumps(response).encode('utf-8'))
                print(f" POST Data received {data}")

            except json.JSONDecodeError:
                # If the received data is not valid JSON, respond with an error
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {"Error": "Invalid JSON data"}
                self.wfile.write(json.dumps(response).encode('utf-8'))
           
               
            except FileNotFoundError:
                self.send_response(404)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {"Error": "File not found"}
                self.wfile.write(json.dumps(response).encode('utf-8')) 

        
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {"Error": f"An error occurred: {str(e)}"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            


def run ():
    try:
        HOST='127.0.0.1'
        PORT=8000
        # Start the server on port 8000
        httpd = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
        print("Server started at http://localhost:8000")
        httpd.serve_forever()
    except Exception as e:
        raise Exception(f"{e}")

if __name__ == "__main__":
   try:
      run()
   except Exception as e:
        print(str(e))
