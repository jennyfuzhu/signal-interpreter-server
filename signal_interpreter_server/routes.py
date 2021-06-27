"""
Routes.py
Style check is 100%
"""
import logging
from flask import Flask, request, jsonify, abort
from json_parser import JsonParser
from exceptions import GetTitleError
log = logging.getLogger(__name__)

json_parser = JsonParser()

signal_interpreter_app = Flask(__name__)


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    """POST function"""
    try:
        data = request.get_json()
        response = json_parser.get_signal_title(data['signal'])
        json_return = jsonify(response)
        data_sig = data['signal']
        log.info("Client sent signal: %s, data", data_sig)
        log.info("Server response title: %s", response)
        return json_return
    except GetTitleError as err:
        log.exception("Exception occurred in title: %s", err)
        abort(404, description="Bad request")
    except KeyError as err:
        log.warning("Exception occurred in POST: %s", err)
        abort(404, description="Page not found")
