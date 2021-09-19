from flask import Flask
from utils import requirements

app = Flask(__name__)


@app.route("/requirements")
def hello_world():
    return requirements()


@app.route("/task_2")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/task_3")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/task_4")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
