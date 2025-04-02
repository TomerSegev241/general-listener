from flask import Flask, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename="requests.log", level=logging.INFO,
                    format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")


def log_request(req):
    client_ip = request.remote_addr
    client_port = request.environ.get('REMOTE_PORT')
    server_ip = request.host.split(':')[0]
    server_port = request.environ.get('SERVER_PORT')

    log_data = (f"{req.method} {req.path} - Client IP: {client_ip}:{client_port} - "
                f"Server IP: {server_ip}:{server_port} - Headers: {dict(req.headers)} - "
                f"Body: {req.get_data(as_text=True)}")
    print("log_data: " + str(log_data))
    app.logger.info(log_data)


@app.before_request
def before_request():
    log_request(request)


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def home():
    log_request(request)
    return "Server is running and logging requests."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Make server accessible from the internet
