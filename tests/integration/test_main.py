# pylint: disable=missing-function-docstring
""" Integration test for main"""
import os
import sys
from unittest.mock import patch
import logging
import pytest
from flask import Flask
from src.routes import signal_interpreter_app
from src.main import main

log = logging.getLogger(__name__)
current_dir = os.path.abspath(os.path.dirname(__file__))
fixture_path = os.path.join(current_dir, "fixtures", "test_basic.json")
this_file_name = os.path.basename(__file__)
log.debug("Current directory: " + current_dir)
log.debug("Fixture path: " + fixture_path)


@pytest.mark.parametrize("file, services_ind, id_ind", [
    (os.path.join(current_dir, "fixtures", "test_basic.json"), "services", "id"),
    (os.path.join(current_dir, "fixtures", "test_basic.xml"), "services/service", "@id"),
])
# @patch.object(Flask, "run")
@patch.object(sys, "argv", ["signal_interpreter_server", "--file_path", fixture_path])
@patch.object(signal_interpreter_app, "run")
def test_main_app(parser, file, services_ind, id_ind):
    """
    This function should test the main method for the signal_interpreter_server program
    It should test the full flow from STARTING the server in main.py
    to returning the correct response of a POST-request

    The test should use the fixture called test_basic.json
    (Make use of fixtures for instantiating classes that you use in multiple
    unit tests
    """
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()
    log.debug("%s: Entering main method of the signal interpreter program" % this_file_name)
    with my_app_instance as client:
        with patch.object(sys, "argv", ["main.main", "--file_path", file]):
            main()
            for data in parser.get_parser().data[services_ind]:
                response = client.post("/", json={"signal":data[id_ind]})
                assert response.get_json() == data["title"]
