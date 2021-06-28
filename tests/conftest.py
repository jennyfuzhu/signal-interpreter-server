"""
Includes all the fixtures

By adding the @pytest.fixture-decorator to your function,
pytest will recognize the function whenever it is used as input parameter in your unit tests.
If you have multiple input parameters, the fixture parameter should be put last.
You therefore do not need to import conftest.py to your unit test.
"""

from signal_interpreter_server.json_parser import JsonParser
import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
print(sys.path)


@pytest.fixture()
def json_parser():
    json_parser = JsonParser()
    return json_parser

