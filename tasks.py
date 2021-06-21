"""tasks.py, using c as Context"""
import os
from invoke import task

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.join(CURR_DIR, "signal_interpreter_server")
UNIT_TEST_DIR = os.path.join(CURR_DIR, "tests", "unit")
COV_PATH = os.path.join(CURR_DIR, ".coveragerc")

@task
def style(c):
    """Style """
    c.run(f"pycodestyle {SRC_DIR} --ignore=E501")


@task
def lint(c):
    """Lint"""
    c.run(f"pylint {SRC_DIR}")


@task
def unit_test(c):
    """Unit tests"""
    cmd = f"pytest {UNIT_TEST_DIR} --cov {SRC_DIR} --cov-config={COV_PATH}"
    c.run(cmd)
