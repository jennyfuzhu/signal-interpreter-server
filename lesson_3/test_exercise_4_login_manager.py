# test_exercise_4_login_manager.py

from unittest.mock import patch
from lesson_3.exercise_4_login_manager import get_credentials


@patch("builtins.print")
@patch("lesson_3.exercise_4_login_manager.login", side_effect=PermissionError)
@patch("builtins.input", side_effect=["bob", "bobocop123"])
def test_get_credentials_with_invalid_credentials(mock_input, mock_login, mock_print):
    get_credentials()
    mock_login.assert_called_with("bob", "bobocop123")
    mock_print.assert_called_with("You do not have permission!")
