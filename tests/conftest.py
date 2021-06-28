"""
Includes all the fixtures

By adding the @pytest.fixture-decorator to your function,
pytest will recognize the function whenever it is used as input parameter in your unit tests.
If you have multiple input parameters, the fixture parameter should be put last.
You therefore do not need to import conftest.py to your unit test.
"""

import sys
from unittest.mock import patch
from signal_interpreter_server.json_parser import JsonParser
import pytest

from signal_interpreter_server.main import main


@pytest.fixture
def json_parser():
    json_parser = JsonParser()
    return json_parser

