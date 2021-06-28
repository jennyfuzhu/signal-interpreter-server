"""Main.py"""
from unittest.mock import patch
from signal_interpreter_server.main import main, parse_arguments, ArgumentParser, init
from signal_interpreter_server.routes import JsonParser, signal_interpreter_app


class MockArgs:  # pylint: disable=too-few-public-methods
    """Class mock args"""
    file_path = "path/to/file"


@patch('signal_interpreter_server.main.main')
@patch('signal_interpreter_server.main.__name__', "__main__")
def test_if_init_name(mock_main):
    init()
    mock_main.assert_called_once()


@patch.object(ArgumentParser, "add_argument")
@patch.object(ArgumentParser, "parse_args", return_value=MockArgs)
def test_parse_arguments(mock_parse_args, mock_add_argument):
    """Function which tests the argument parser, from lesson 2"""
    assert parse_arguments() == MockArgs
    mock_parse_args.assert_called_once()
    mock_add_argument.assert_called_with("--file_path")


@patch.object(signal_interpreter_app, 'run')
@patch.object(JsonParser, 'load_file')
@patch('signal_interpreter_server.main.parse_arguments', return_value=MockArgs)
def test_main(mock_parse_arguments, mock_load_file, mock_run):
    """Function which tests the main function"""
    main()
    mock_parse_arguments.assert_called_once()
    mock_load_file.assert_called_with(MockArgs.file_path)
    mock_run.assert_called_once()
