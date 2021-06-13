from lesson_3.exercise_4.capitals import get_capital, practice_capitals
from unittest.mock import patch


@patch("lesson_3.exercise_4.capitals.get_capital", return_value="Stockholm")
@patch("builtins.print")
# The input to the function should be Sweden
@patch("builtins.input", side_effect=["Sweden"])
def test_practice_capital_exists(mock_input, mock_print, mock_get_capital):
    practice_capitals()
    mock_get_capital.assert_called_with("Sweden")
    mock_print.assert_called_with("The capital of Sweden is Stockholm")


@patch("lesson_3.exercise_4.capitals.get_capital", return_value="RANDOM")
@patch("builtins.print")
# suppose to throw a key error
@patch("builtins.input", side_effect=["RANDOM_COUNTRY"])
def test_practice_capital_not_exist(mock_input, mock_print, mock_get_capital):
    practice_capitals()
    mock_get_capital.assert_called_with("RANDOM_COUNTRY")
    mock_print.assert_called_with("RANDOM_COUNTRY does not exist in our dictionary")
