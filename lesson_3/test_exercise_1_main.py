# test_main.py

from unittest.mock import patch
from lesson_3.exercise_1_main import main, init


@patch("builtins.print")
def test_main(mock_print):
    main()
    mock_print.assert_called_with("Hello world!")

# Decorator
@patch("lesson_3.exercise_1_main.main")
@patch("lesson_3.exercise_1_main.__name__", "__main__")
def test_init(mock_main):
    init()
    mock_main.assert_called_once()

# Context manager
def test_init():
    with patch("lesson_3.exericse_1.main.main") as mock_main:
        with patch("lesson_3.exercise_1.main.__name__", "__main__"):
            init()
            mock_main.assert_called_once()
