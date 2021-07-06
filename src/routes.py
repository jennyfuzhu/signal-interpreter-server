"""
Handles connection to flask server.
"""
import logging
from flask import Flask, request, jsonify, abort
from src.json_parser import JsonParser
from src.exceptions import JsonError, XmlError
from src.parser_factory import ParseFactory


log = logging.getLogger(__name__)

json_parser = JsonParser() # Not used atm because of the generic parser

signal_interpreter_app = Flask(__name__)

parse_factory = ParseFactory()


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    """POST function"""
    try:
        data = request.get_json()
        parser = parse_factory.get_parser()
        response = parser.get_signal_title(data['signal'])
        log.info("Server response title: %s", response)
        return jsonify(response)
    except KeyError as err:
        log.exception("Exception occurred in title: %s", err)
        abort(400, description="Bad request")
    except JsonError as err:
        log.exception("Exception occurred in post function: %s", err)
        abort(404, description="Interpreter for data not avalible")
    except XmlError as err:
        log.exception("Exexption occurred, error recevied: %s", err)
        abort(202, description="Interpreter for data not avalible")

