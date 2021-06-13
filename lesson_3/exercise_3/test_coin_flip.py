from unittest.mock import patch, call
from lesson_3.exercise_3.coin_flip import get_three_heads


def test_get_three_heads():
    with 'lesson_3.exercise_3.coin_flip.random.choice' as mock_random_choice:
        with patch("builtins.print") as mock_print:
            mock_random_choice.side_effect = ["heads", "heads", "tails", "heads"]
            get_three_heads()
            assert mock_print.mock_calls == [call("Got heads"),
                                             call("Got heads"),
                                             call("Got tails"),
                                             call("Got heads"),
                                             call("Number of tries until three heads: 4")]
