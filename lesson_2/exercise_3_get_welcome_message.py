# exercise_3_get_welcome_message.py
from unittest.mock import patch
import unittest
from lesson_2.exercise_2_get_name_from_user import get_name_from_user


def get_welcome_message():
    name = get_name_from_user()
    welcome_message = f"Welcome {name}!"
    return welcome_message


class Lesson2:

    @patch("lesson_2.exercise_2_get_name_from_user.get_name_from_user", return_value="Jimbo")
    def test_get_welcome_message(self, mock_get_name_from_user):
        assert get_welcome_message() == f"Welcome {mock_get_name_from_user()}!"


if __name__ == '__main__':
    unittest.main()
