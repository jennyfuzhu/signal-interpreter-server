from unittest.mock import patch
from source.main import main, ArgumentParser, parse_arguments
from source.routes import JsonParser, signal_interpreter_app


class MockArgs:
    file_path = "path/to/file"


@patch.object(signal_interpreter_app, 'run')
@patch.object(JsonParser, 'load_file')
@patch('source.main.parse_arguments', return_value=MockArgs)
def test_main(mock_parse_arguments, mock_load_file, mock_run):
    main()

    mock_parse_arguments.assert_called_once()
    mock_load_file.assert_called_with(MockArgs.file_path)
    mock_run.assert_called_once()
