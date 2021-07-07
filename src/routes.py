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
    data = request.get_json()
    try:
        response = json_parser.get_signal_title(data['signal'])
        log.info("Server response title: %s", response)
        return jsonify(response)
    except KeyError as err:
        log.exception("Exception occurred in title: %s", err)
        abort(400, description=f"Payload {data} is not correct, expects the key to be 'signal")
    except JsonError as err:
        log.exception("Exception occurred in post function: %s", err)
        abort(404, description=f"Interpretation for {data['signal']} not available.")
    #except XmlError as err:
        #log.exception("Exexption occurred, error recevied: %s", err)
        #abort(404, description="Interpreter for data not avalible")

