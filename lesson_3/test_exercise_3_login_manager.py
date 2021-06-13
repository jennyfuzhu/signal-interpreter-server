# test_exercise_3_login_manager.py

from unittest.mock import patch
from lesson_3.exercise_3_login_manager import get_credentials


@patch("lesson_3.exercise_3_login_manager.login")
@patch("builtins.input", side_effect=["bob", "bobocop123"])
def test_get_credentials(mock_input, mock_login):
    get_credentials()
    mock_login.assert_called_with("bob", "bobocop123")
