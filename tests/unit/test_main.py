# pylint: disable=missing-function-docstring
"""Main.py"""
import sys
import json
import logging
import os

import pytest
from flask import Flask
from unittest.mock import patch
from src.main import main, parse_arguments, ArgumentParser, init, parse_factory, extract_extension
from xml_parser import XmlParser
from src.routes import JsonParser, signal_interpreter_app
from src.parser_factory import ParseFactory

json_test = 'signal_database.json'
xml_test = 'database/sdb.xml'
this_file_name = os.path.basename(__file__)
log = logging.getLogger(__name__)


class MockArgs:  # pylint: disable=too-few-public-methods
    """Class mock args"""
    file_path = "python_step3\signal_database.json"


@patch('src.main.main')
@patch('src.main.__name__', "__main__")
def test_if_init_name(mock_main):
    init()
    mock_main.assert_called_once()


@patch.object(signal_interpreter_app, 'run')
@patch.object(JsonParser, 'load_file')
@patch.object(ParseFactory, "get_parser")
@patch.object(JsonParser, "get_signal_title")
@patch.object(Flask, "run")
@patch('src.main.extract_extension')
@patch('src.main.parse_arguments')
def test_main(mock_parse_arguments, mock_extract_extension, mock_run, mock_load_file, mock_get_signal_title,
              mock_get_parser, parse_factory_instance, json_parser):
    """Function which tests the main function"""
    parse_factory_instance.register_format(".json", JsonParser)
    parse_factory_instance.set_signal_datbase_format(".json")
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()
    mock_parse_arguments.return_value = json_test
    mock_extract_extension.return_value = ".json"
    mock_get_parser.return_value = json_parser
    mock_get_signal_title = "foo"
    with my_app_instance as client:
        main()
        pay_load = {"signal": "11"}
        client.post("/", json=pay_load)
        mock_run.assert_called_once()
        mock_load_file.assert_called_with(json_test)


@pytest.mark.parametrize("file_path, extension", [
    ("foo.json", ".json"),
    ("foo.xml", ".xml")
])
def test_extract_extension(file_path, extension):
    """Test extract extension"""
    log.debug("Entering %s unit test" % this_file_name)
    assert extract_extension(file_path) == extension


@patch.object(sys, "argv", ["src", "-f", json_test])
def test_parse_arguments():
    """Test parse arguments"""
    assert parse_arguments() == json_test
