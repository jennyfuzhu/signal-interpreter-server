"""
tasks.py, tasks to perform, style lint and test
ignoring first parameter by setting it to an underscore
The possibility to invoke integration tests is among other things available here
"""
import os
from subprocess import call
from invoke import task

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.join(CURR_DIR, "python_step3")
UNIT_TEST_DIR = os.path.join(CURR_DIR, "tests", "unit")
COV_PATH = os.path.join(CURR_DIR, ".coveragerc")
INTEGRATION_DIR = os.path.join(CURR_DIR, "tests", "integration")
TESTS_DIR = os.path.join(CURR_DIR, "tests")

print(f"Current dir: {CURR_DIR}\nSource dir: {SRC_DIR}\nUnit test dir: {UNIT_TEST_DIR}\nCov path: {COV_PATH}")


@task
def style(_):
    """Style """
    call(f"pycodestyle{SRC_DIR}--ignore=E501", shell=True)


@task
def style_test(_):
    """Style test check"""
    call(f"pycodestyle{TESTS_DIR}--ignore=E501", shell=True)


@task
def lint(_):
    """Lint"""
    call(f"pylint {SRC_DIR}", shell=True)


@task
def lint_test(_):
    call(f"pylint {TESTS_DIR}", shell=True)


@task
def unit_test(_):
    """Unit tests"""
    cmd = f"pytest {UNIT_TEST_DIR} --cov {SRC_DIR} --cov--config={COV_PATH}"
    call(cmd, shell=True)


@task()
def integration_test(_):
    "Integration test"
    cmd = f"python -m pytest {INTEGRATION_DIR} --cov {SRC_DIR} --cov-config={COV_PATH}  --cov-fail-under=75"
    call(cmd, shell=True)
