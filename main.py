from wsgiref import simple_server
import os
from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    message = 'Version 2.0 Deployed on Heroku using Circle CI.'
    return "<h1>{}</h1>".format(message)

port = int(os.getenv("PORT", 5000))
if __name__ == "__main__":
    host = '0.0.0.0'
    # port = 5000
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()
