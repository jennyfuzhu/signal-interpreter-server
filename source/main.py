from source.routes import signal_interpreter_app
from argparse import ArgumentParser
from source.routes import json_parser

def parse_arguments():
    parser = ArgumentParser()
    # the path to the signal database file
    parser.add_argument("--file_path", required=False)

def main():
    args = parse_arguments()
    print(args.file_path)

    # instance of json parser class
    json_parser_class = json_parser.JsonParser
    # load file is being called
    json_parser_class.load_file()

    signal_interpreter_app.run(args.file_path)


if __name__ == '__main__':
    main()
