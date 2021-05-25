# routes.py
from flask import Flask

my_app = Flask(__name__)


@my_app.route("/", methods=["GET"])
def hello():
    return "Hello world!"


my_app.run()