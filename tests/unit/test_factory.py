# pylint: disable=missing-function-docstring
# pylint: disable=protected-access
import logging
import pytest
from src.json_parser import JsonParser
from src.xml_parser import XmlParser


logger = logging.getLogger(__name__)


@pytest.mark.parametrize("data_format", [
    ".json",
    ".xml",
])
def test_set_signal_database_format(parse_factory_instance, data_format):
    """
    Test set format method.
    :param parse_factory_instance:
    :param data_format:
    :param parser_class:
    :return:
    """
    logger.debug("Start of %s function test log.", test_set_signal_database_format.__name__)
    parse_factory_instance.set_signal_database_format(data_format)
    assert parse_factory_instance._signal_database_format == data_format
    logger.debug("End of %s function test log.", test_set_signal_database_format.__name__)


@pytest.mark.parametrize("data_format, parser_class", [
    (".json", JsonParser),
    (".xml", XmlParser)
])
def test_register_format(parse_factory_instance, data_format, parser_class):
    """
    Test register format method.
    :param parse_factory_instance:
    :param data_format:
    :param parser_class:
    :return:
    """
    logger.debug("Start of %s function test log.", test_register_format.__name__)
    parse_factory_instance.register_format(data_format, parser_class)
    assert isinstance(parse_factory_instance._parsers[data_format], parser_class)  # different instances
    logger.debug("End of %s function test log.", test_register_format.__name__)


@pytest.mark.parametrize("data_format, parser_class", [
    (".json", JsonParser),
    (".xml", XmlParser)
])
def test_get_parser(parse_factory_instance, data_format, parser_class):
    """
    Testing get parser.
    :param mock_get_signal_title_from_id:
    :param sig:
    :return:
    """
    logger.debug("Start of %s function test log.", test_get_parser.__name__)
    # parse_factory_instance.register_format(data_format, parser_class)
    # parse_factory_instance.set_signal_database_format(data_format)
    parse_factory_instance._parsers[data_format] = parser_class()  # why mock function when we can set value
    parse_factory_instance._signal_database_format = data_format  # why mock function when we can set value
    assert isinstance(parse_factory_instance.get_parser(), parser_class)  # different instances
    logger.debug("End of %s function test log.", test_get_parser.__name__)


@pytest.mark.parametrize("data_format", [
    ".lol",
])
def test_get_parser_exception(parse_factory_instance, data_format):
    """
    Testing get parser exception.
    :param parse_factory_instance:
    :param data_format:
    :return:
    """
    logger.debug("Start of %s function test log.", test_get_parser.__name__)
    with pytest.raises(ValueError):
        parse_factory_instance._signal_database_format = data_format  # why mock function when we can set value
        parse_factory_instance.get_parser()
    logger.debug("End of %s function test log.", test_get_parser.__name__)