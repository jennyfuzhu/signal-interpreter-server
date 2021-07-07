"""test_interpret_signal.py file"""

from unittest.mock import patch

from src.routes import signal_interpreter_app, JsonParser, parse_factory, JsonError
from src.parser_factory import ParseFactory



def test_interpret_signal_with_valid_signal(signal_interpreter_app_instance):
    with patch.object(JsonParser, "get_signal_title", return_value="") as mock_get_signal_title:
        with signal_interpreter_app_instance as client:
            payload = {"signal": "11"}
            client.post("/", json=payload)
            mock_get_signal_title.assert_called_with("11")


def test_interpret_signal_with_invalid_key(signal_interpreter_app_instance):
    with signal_interpreter_app_instance as client:
        payload = {"dummy": "11"}
        assert client.post("/", json=payload).status_code == 400


def test_interpret_signal_with_invalid_identifier(signal_interpreter_app_instance):
    with signal_interpreter_app_instance as client:
        with patch.object(JsonParser, "get_signal_title", side_effect=JsonError):
            with patch.object(parse_factory, "get_parser", return_value=JsonParser):
                response = client.post("/", json={"signal":"99"})
                assert response.get_json() is None
                assert response.status_code == 404
