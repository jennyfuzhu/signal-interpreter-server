"""test_interpret_signal.py file"""

from unittest.mock import patch
from source.routes import signal_interpreter_app, JsonParser


def test_interpreter_signal():
    """Test the interpret signal"""
    signal_interpreter_app.testing = True
    signal_interpreter_app_ins = signal_interpreter_app.test_client()
    with patch.object(JsonParser, 'get_signal_title',
                      return_value='Transfer Data') as mock_get_signal_title:
        with signal_interpreter_app_ins as client:
            test_payload = {'signal': '36'}
            response = client.post('/', json=test_payload)
            mock_get_signal_title.assert_called_with('36')
            assert response.get_json() == 'Transfer Data'
