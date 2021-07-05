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
        """
        Loading an XML-file and converting it to a dictionary
        :param file_path:
        :return:

        """
        tree = ET.parse(file_path)
        data = tree.getroot()
        xml_string = ET.tostring(data, encoding="utf-8", method="xml")
        data = dict(xmltodict.parse(xml_string))
