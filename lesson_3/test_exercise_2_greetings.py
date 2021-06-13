# test_exercise_2_greetings.py

from unittest.mock import patch, call
from lesson_3.exercise_2_greetings import print_hello_and_goodbye


@patch("builtins.print")
def test_print_hello_and_goodbye(mock_print):
    print_hello_and_goodbye()
    assert mock_print.mock_calls == [call("Hello"), call("Goodbye")]
