"""
Includes all the fixtures

By adding the @pytest.fixture-decorator to your function,
pytest will recognize the function whenever it is used as input parameter in your unit tests.
If you have multiple input parameters, the fixture parameter should be put last.
You therefore do not need to import conftest.py to your unit test.
"""

from src.json_parser import JsonParser
import pytest
from src.parser_factory import ParseFactory
from src.routes import signal_interpreter_app


@pytest.fixture
def json_parser():
    json_parser = JsonParser()
    return json_parser

@pytest.fixture
def parse_factort_instace():
    parser_factory = ParseFactory()
    return parser_factory

@pytest.fixture
def signal_interpreter_app_instance():
    signal_interpreter_app.testing = True
    return signal_interpreter_app.test_client()
