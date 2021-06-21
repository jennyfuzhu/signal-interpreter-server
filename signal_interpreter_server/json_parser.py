"""Json_parser.py
    Style check 100%
"""
import json


class JsonParser:
    """Class which contains methods of json functions"""

    def __init__(self):
        self.data = None
        self.signal_title = ""

    def load_file(self, file_path):
        """Load files with the path to the file as an argument"""
        # open the json file
        # load the json file and save it to self.data
        with open(file_path, 'r') as my_file:
            self.data = json.load(my_file)

    def get_signal_title(self, identifier):
        """Return the title of the identifier"""
        # loop through all services in self.data
        # if the service ID is the identifier, return the title
        for names in self.data['services']:
            if names['id'] == identifier:
                self.signal_title = names['title']
                return self.signal_title
        return f"{identifier} not found"
