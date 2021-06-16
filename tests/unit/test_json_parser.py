"""test_json_parser.py
    Lint check 100%
    """
from unittest.mock import patch, mock_open

import pytest

from signal_interpreter_server.json_parser import JsonParser

INPUT_JSON = '{"json": "json Jsonsson"}'
OUTPUT_JSON = {"json": "json Jsonsson"}

json_parser_class = JsonParser()
json_parser_class.data = {"services": [{"title": "ECU Reset", "id": "11"}, {"title": "Security Access", "id": "27"},
                                       {"title": "Tester Present", "id": "3E"}, {"title": "None", "id": "20"}]}


def test_load_file():
    """Test load file function """
    with patch("builtins.open", mock_open(read_data=INPUT_JSON)):
        json_parser_class_tlf = JsonParser()
        json_parser_class_tlf.load_file('random/path')
        assert json_parser_class_tlf.data == OUTPUT_JSON


def test_get_signal_title():
    """Test get signal title function"""
    json_parser_class_tlt = JsonParser()
    json_parser_class_tlt.data = {'services': [{'title': 'ECU Reset', 'id': '11'}]}
    assert json_parser_class_tlt.get_signal_title('11') == "ECU Reset"

# Need at least two signals
@pytest.mark.parametrize("item, expected_title", [
    ("11", "ECU Reset"),
    ("27", "Security Access"),
    ("3E", "Tester Present"),
])
def test_get_signal_tite_paramatrize(item, expected_title):
    assert json_parser_class.get_signal_title(item) == expected_title
