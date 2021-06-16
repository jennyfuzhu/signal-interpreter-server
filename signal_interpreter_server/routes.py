"""Routes.py
    Style check
"""

from flask import Flask, request, jsonify
from signal_interpreter_server.json_parser import JsonParser

json_parser = JsonParser()

signal_interpreter_app = Flask(__name__)


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    """Return json"""
    data = request.get_json()
    response = json_parser.get_signal_title(data['signal'])
    json_return = jsonify(response)
    return json_return
