from source.main import parse_arguments, ArgumentParser
from unittest.mock import patch


class TestMockArgs:
    file_path = "path/to/file"


@patch.object(ArgumentParser, "add_argument")
@patch.object(ArgumentParser, "parse_args", return_value=TestMockArgs)
def test_parse_arguments(mock_parse_args, mock_add_argument):
    assert parse_arguments() == TestMockArgs
    mock_parse_args.assert_called_once()
    mock_add_argument.assert_called_with("--file_path")
