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
    parser.add_argument("-f","--file_path", help='Path to the sdb file')
    args =parser.parse_args()
    return args.file_path

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
    log.info("Entering the main function of the program.")
    db_path = parse_arguments()
    db_type = extract_extension(db_path)
    log.info("DB type: " + db_type)

    if db_path:
        log.info("Initiating path to file: " + db_path)
    else:
        print("ERROR: No path specified, terminating program...")
        sys.exit()


    parse_factory.set_signal_database_format(db_type)
    server_parser = parse_factory.get_parser()
    server_parser.load_file(db_path)

    #json_parser.load_file(args.file_path)

    log.info("Staring server.")
    signal_interpreter_app.run()
    log.info("Program finished.")


def init():  # pylint: disable=missing-function-docstring
    if __name__ == '__main__':
        main()


init()
