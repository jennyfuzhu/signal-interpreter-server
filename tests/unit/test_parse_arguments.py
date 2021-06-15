"""test_parse_arguments.py"""
from unittest.mock import patch
from source.main import parse_arguments, ArgumentParser


class MockArgs:  # pylint: disable=too-few-public-methods
    """Class mock args"""
    file_path = "path/to/file"


@patch.object(ArgumentParser, "add_argument")
@patch.object(ArgumentParser, "parse_args", return_value=MockArgs)
def test_parse_arguments(mock_parse_args, mock_add_argument):
    """Function which test the parse argument function"""
    assert parse_arguments() == MockArgs
    mock_add_argument.assert_called_with("--file_path")
    mock_parse_args.assert_called_once()
