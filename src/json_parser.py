"""Json_parser.py"""
import json
import logging
from src.exceptions import JsonError, GetTitleError

log = logging.getLogger(__name__)


class JsonParser:
    """Class which contains methods of json functions"""

    def __init__(self):
        self.data = None
        self.signal_title = ""

    def load_file(self, file_path):
        """Load files with the path to the file as an argument"""
        try:
            with open(file_path, 'r') as my_file:
                self.data = json.load(my_file)
                log.info("Loaded json file %s", file_path)
        except FileNotFoundError as err:
            log.exception("Exception occurred. Could not load json file: %s", err)
            raise JsonError from err

    def get_signal_title(self, identifier):
        """Return the title of the identifier"""
        try:
            for names in self.data['services']:
                if names['id'] == identifier:
                    self.signal_title = names['title']
                    return self.signal_title
            return f"{identifier} not found"
        except KeyError as err:
            log.exception("Exception occurred %s", err)
            raise GetTitleError from err
