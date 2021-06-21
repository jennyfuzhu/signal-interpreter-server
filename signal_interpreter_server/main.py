"""
This is the main program of the signal-interpreter program.
"""
from argparse import ArgumentParser
from signal_interpreter_server.routes import json_parser, signal_interpreter_app


def parse_arguments():
    """Parse arguments"""
    parser = ArgumentParser()
    # the path to the signal database file
    parser.add_argument("--file_path")
    return parser.parse_args()


def main():
    """Main function"""
    args = parse_arguments()
    print(args.file_path)

    # instance of json parser class
    # json_parser_class = JsonParser()
    # Du använder JsonParser klassen fel
    # Du ska instantiera den i routes och sedan använda det objektet.
    # load file is being called
    json_parser.load_file(args.file_path)

    signal_interpreter_app.run()


def init(): # pylint: disable=missing-function-docstring
    if __name__ == '__main__':
        main()


init()
