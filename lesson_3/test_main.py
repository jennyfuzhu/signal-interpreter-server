# test_main.py

from unittest.mock import patch
from lesson_3.main import main, init


@patch("builtins.print")
def test_main(mock_print):
    main()
    mock_print.assert_called_with("Hello world!")