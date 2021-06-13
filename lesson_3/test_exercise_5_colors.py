# test_exercise_5_colors.py

import pytest
from lesson_3.exercise_5_colors import is_color


def test_is_color_with_valid_color():
    assert is_color("blue")


def test_is_color_with_mixed_casing():
    assert is_color("YeLLoW")


def test_is_color_with_punctuation():
    assert is_color("red.")


@pytest.mark.parametrize("color, expected_result", [
    ("blue", True),
    ("YeLLoW", True),
    ("red.", True),
    ("ball", False),
    ("", False),
])
def test_is_color(color, expected_result):
    assert is_color(color) == expected_result
