""" Integration test for main"""
import os
import sys
from unittest.mock import patch
import logging
import pytest
from flask import Flask
from signal_interpreter_server.routes import signal_interpreter_app
from signal_interpreter_server.main import main

log = logging.getLogger(__name__)
current_dir = os.path.abspath(os.path.dirname(__file__))
fixture_path = os.path.join(current_dir, "fixtures", "test_basic.json")
log.debug("Current directory: " + current_dir)
log.debug("Fixture path: " + fixture_path)


@patch.object(sys, "argv", ["signal_interpreter_server", "--file_path", fixture_path])
@patch.object(signal_interpreter_app, "run")
def test_main_app(mock):
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

    main()
    mock.assert_called_once()
    with my_app_instance as client:
        test_payload = {"signal": "27"}
        response = client.post("/", json=test_payload)
        assert response.get_json() == "Security Access"
