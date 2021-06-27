"""This is the main program of the signal-interpreter program.
    Style check 100%
"""
from argparse import ArgumentParser
from json_parser import JsonParser
from routes import signal_interpreter_app


def parse_arguments():
    """Parse arguments"""
    parser = ArgumentParser()
    # the path to the signal database file
    parser.add_argument("--file_path")
    return parser.parse_args()


def main():  # pylint: disable=missing-function-docstring
    """Main function"""
    args = parse_arguments()
    print(args.file_path)

    # instance of json parser class
    json_parser_class = JsonParser()
    # load file is being called
    json_parser_class.load_file(args.file_path)

    signal_interpreter_app.run()


def init():  # pylint: disable=missing-function-docstring
    if __name__ == '__main__':
        main()


init()
