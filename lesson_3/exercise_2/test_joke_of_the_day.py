from unittest.mock import patch, call

from lesson_3.exercise_2.joke_of_the_day import joke_of_the_day
"""
The unit tests should mock both the input-function and the print-function
 and asserting that the print-function gets called with the correct parameters
"""

@patch("builtins.print")
def test_joke_of_the_day_wrong_answer(mock_print):
    with patch("builtins.input", return_vale="No se"):
        joke_of_the_day()
        assert mock_print.mock_calls == [
            call("---Joke of the day---"), call("Wrong answer! The correct answer is 'Duck!'")]


@patch("builtins.print")
def test_joke_of_the_day_correct_answer(mock_print):
    with patch("builtins.input", return_value="Duck"):
        joke_of_the_day()
        assert mock_print.mock_calls == [call("---Joke of the day---"), call("Correct!")]
