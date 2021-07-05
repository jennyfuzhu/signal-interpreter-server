"""This is the main program of the signal-interpreter program."""
import logging
import sys
import os

from argparse import ArgumentParser
from src.routes import signal_interpreter_app, json_parser, parse_factory
from src.xml_parser import XmlParser
from src.json_parser import JsonParser

log = logging.getLogger(__name__)

parse_factory.register_format(".json", JsonParser)
parse_factory.register_format(".xml", XmlParser)

def parse_arguments():
    """Parse arguments"""
    parser = ArgumentParser()
    # the path to the signal database file
    parser.add_argument("--file_path", help='Path to the sdb file')
    return parser.parse_args()

def extract_extension(file_path):
    filename, extension = os.path.splitext(file_path)
    return extension
    """
    Return the file type
    :param file_path:
    :return:
    """

def main():
    """Main function"""
    args = parse_arguments()
    log.info("Entering the main function of the program.")
    db_type = extract_extension(args.file_path)
    log.info("DB type: " + db_type)

    if args.file_path:
        log.info("Initiating path to file: " + args.file_path)
    else:
        print("ERROR: No path specified, terminating program...")
        sys.exit()


    parse_factory.set_signal_database_format(db_type)
    server_parser = parse_factory.get_parser()
    server_parser.load_file(args.file_path)

    #json_parser.load_file(args.file_path)

    log.info("Staring server.")
    signal_interpreter_app.run()
    log.info("Program finished.")


def init():  # pylint: disable=missing-function-docstring
    if __name__ == '__main__':
        main()


init()
