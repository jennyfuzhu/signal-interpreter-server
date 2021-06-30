"""Init file of source folder """
import logging.config
import yaml
import os

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
LOG_CONFIG_PATH = os.path.join(CURR_DIR, "..", "cfg", "log_config.yaml")
FIXTURE_PATH = os.path.join(CURR_DIR, "..", "fixtures", "test_basic.json")
UNIT_TEST_DIR = os.path.join(CURR_DIR, "tests", "unit")

with open(LOG_CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
