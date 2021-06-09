import os
import unittest
from unittest.mock import patch, mock_open
from source.json_parser import JsonParser
import json

json_parser_class = JsonParser()
json_parser_class.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
"""


"""
class TestJsonParser(unittest.TestCase):

    def test_load_file(self, tmp):
        with patch("builtins.open", mock_open(read_data="Hello")):
            tempt_data = {"services": [{"title": "ECU Reset", "id": "11"}]}
            file_path = os.path.join(tmp, "temp_json.json")

            with open(file_path, 'w') as json_file:
                json.dump(tempt_data, json_file)

            json_parser_class.load_file(file_path)
            assert isinstance(json_parser_class.data, dict)

            assert json_parser_class.data == tempt_data

    def test_get_signal_title(self):
        assert json_parser_class.get_signal_title(11) == "ECU reset"
