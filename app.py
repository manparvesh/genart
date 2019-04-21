from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"


if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
