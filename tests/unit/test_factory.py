# pylint: disable=missing-function-docstring
# pylint: disable=protected-access
import logging
from src.parser_factory import ParseFactory

log = logging.getLogger(__name__)
parse_factory = ParseFactory()

class MockParser:
    """Mock parser class"""


def test_set_signal_database_format():
    """Test set signal database format unit test"""
    log.debug("Entering %s unit test" % test_set_signal_database_format.__name__)
    parse_factory.set_signal_database_format("EXTENSION")
    assert parse_factory._signal_database_format == "EXTENSION"
    log.debug("Existing %s unit test" % test_set_signal_database_format.__name__)


def test_register_format():
    "Test register format unit test"
    log.debug("Entering %s unit test:" % test_register_format.__name__)
    parse_factory.register_format("FORMAT", MockParser)
    assert isinstance(parse_factory._parsers["FORMAT"], MockParser)
    log.debug("Exiting %s unit test" % test_register_format.__name__)


def test_get_parser():
    """Test get parser unit test"""
    log.debug("Entering %s unit test:" % test_get_parser.__name__)
    parse_factory._parsers["EXTENSION"] = MockParser
    parse_factory._signal_database_format = "EXTENSION"
    assert parse_factory.get_parser() == MockParser
    log.debug("Exiting %s unit test:" % test_get_parser.__name__)
