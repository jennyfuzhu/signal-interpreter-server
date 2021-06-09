# routes.py

from flask import Flask, request, jsonify
from source.json_parser import JsonParser

json_parser = JsonParser()

signal_interpreter_app = Flask(__name__)


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    data = request.get_json()
    response = json_parser.get_signal_title(data['signal'])
    json_return = jsonify(response)
    return json_return
