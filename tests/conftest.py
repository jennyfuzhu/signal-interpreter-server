"""Will be used later in wee k4
Includes all the fixtures
Separate test data from the test cases


By adding the @pytest.fixture-decorator to your function,
pytest will recognize the function whenever it is used as input parameter in your unit tests.
If you have multiple input parameters, the fixture parameter should be put last.
You therefore do not need to import conftest.py to your unit test.
"""

# conftest.py
import pytest


@pytest.fixture
def fruits_and_vegetables():
    pass