from source.routes import interpret_signal, request
from source.routes import signal_interpreter_app, JsonParser
from unittest.mock import patch


def test_interpreter_signal():
    signal_interpreter_app.testing = True
    signal_interpreter_app_ins = signal_interpreter_app.test_client()
    with patch.object(JsonParser, 'get_signal_title', return_value = 'ECU Reset') as mock_get_signal_title:
        with signal_interpreter_app_ins as client:
            test_payload = {'signal':'11'}
            response = client.post('/', json=test_payload)
            mock_get_signal_title.assert_called_with('11')
            assert response.get_json() == 'ECU Reset'
