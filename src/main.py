"""This is the main program of the signal-interpreter program."""
import logging
import sys

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


def main():
    """Main function"""
    log.info("Entering the main function of the program.")
    args = parse_arguments()
    if args.file_path:
        log.info("Initiating path to file: " + args.file_path)
    else:
        print("ERROR: No path specified, terminating program...")
        sys.exit()

    json_parser.load_file(args.file_path)
    log.info("Staring server.")
    signal_interpreter_app.run()
    log.info("Program finished.")


def init():  # pylint: disable=missing-function-docstring
    if __name__ == '__main__':
        main()


init()
