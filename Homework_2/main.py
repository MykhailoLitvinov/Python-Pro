from flask import Flask, request
from utils import requirements, generate_users, mean, open_csv, space

app = Flask(__name__)


@app.route("/requirements")
def get_requirements():
    return requirements()


@app.route("/generate_users")
def get_user():
    num = request.args.get('num', '10')
    if num.isdigit():
        num = int(num)
    return generate_users(num)


@app.route("/mean")
def get_mean():
    return mean(open_csv())


@app.route("/space")
def get_space():
    return space()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
