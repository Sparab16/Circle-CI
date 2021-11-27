from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    message = 'Circle CI Demonstation number 2'
    return "<h1>{}</h1>".format(message)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
    