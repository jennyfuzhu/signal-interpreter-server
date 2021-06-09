# routes.py

from flask import Flask, request, jsonify
from source.json_parser import JsonParser

json_parser = JsonParser()

signal_interpreter_app = Flask(__name__)


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    data = request.get_json()

    signal_title = json_parser.get_signal_title(data["signal"])
    return jsonify(signal_title=signal_title).get_json()
