"""test_json_parser.py"""
from unittest.mock import patch, mock_open
from source.json_parser import JsonParser

INPUT_JSON = '{"json": "json Jsonsson"}'
OUTPUT_JSON = {"json": "json Jsonsson"}


def test_load_file():
    """Test load file function """
    with patch("builtins.open", mock_open(read_data=INPUT_JSON)):
        json_parser_class = JsonParser()
        json_parser_class.load_file('random/path')
        assert json_parser_class.data == OUTPUT_JSON


def test_get_signal_title():
    """Test get signal title function"""
    json_parser_class = JsonParser()
    json_parser_class.data = {'services': [{'title': 'ECU Reset', 'id': '11'}]}
    assert json_parser_class.get_signal_title('11') == "ECU Reset"
