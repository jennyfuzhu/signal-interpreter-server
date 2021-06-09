# test_json_parser.py
from unittest.mock import patch, mock_open
from source.json_parser import JsonParser

input_json = '{"json": "Json Jsonsson"}'
output_json = {"json": "Json Jsonsson"}


def test_load_file():
    with patch("builtins.open", mock_open(read_data=input_json)):
        json_parser_class = JsonParser()
        json_parser_class.load_file('random/path')
        assert json_parser_class.data == output_json


def test_get_signal_title():
    json_parser_class = JsonParser()
    json_parser_class.data = {'services': [{'title': 'ECU Reset', 'id': '11'}]}
    assert json_parser_class.get_signal_title('11') == "ECU Reset"
