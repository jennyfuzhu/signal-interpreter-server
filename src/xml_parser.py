"""Class for parsing xml"""
import xml.etree.ElementTree as ET
import xmltodict
import logging

log = logging.getLogger(__name__)


class XmlParser:
    """Class for loading and parsing the signal database with XML"""

    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        """Loading an XML-file and converting it to a dictionary"""
        try:
            tree = ET.parse(file_path)
            data = tree.getroot()
            xml_string = ET.tostring(data, encoding="utf-8", method="xml")
            data = dict(xmltodict.parse(xml_string))
        except FileNotFoundError as e:
            log.exception("Exception raised, could not fins %s " %file_path)

    def get_signal_title(self, identifier):
        """ Get signal title method."""
        for services in self.data["services"].values():
            for service in services:
                if service["@id"] == identifier:
                    return service["title"]
