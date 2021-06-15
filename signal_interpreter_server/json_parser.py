"""Json_parser.py"""
import json


class JsonParser:
    """Class which contains methods of json functions"""
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        """Load files with the path to the file as an argument"""
        # open the json file
        # load the json file and save it to self.data
        with open(file_path, 'r') as my_file:
            self.data = json.load(my_file)
            print(self.data)

    def get_signal_title(self, identifier):
        """Return the title of the identifier"""
        # loop through all services in self.data
        # if the service ID is the identifier, return the title
        for names in self.data['services']:
            if str(identifier) == names['id']:
                signal_title = names['title']
        return signal_title
