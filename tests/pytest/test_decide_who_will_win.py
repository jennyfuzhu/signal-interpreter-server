# test_decide_who_will_win
import unittest
from unittest.mock import patch

from tests.pytest.rock_paper_scissor_game import RandomClass

random_class = RandomClass()

tie = "It was a tie"
players_win = "You won!"
computer_win = "You lost."
choices_list = ["rock", "paper", "scissor"]


class TestDecideWhoWillWin(unittest.TestCase):

    def test_decide_who_will_win_rock_scissor(self):
        assert decide_who_will_win("rock", "scissor") == players_win

    def test_decide_who_will_win_rock_rock(self):
        assert decide_who_will_win("rock", "rock") == tie

    def test_decide_who_will_win_rock_paper(self):
        assert decide_who_will_win("rock", "paper") == computer_win

    def test_decide_who_will_win_paper_paper(self):
        assert decide_who_will_win("paper", "paper") == tie

    def test_decide_who_will_win_paper_rock(self):
        assert decide_who_will_win("paper", "rock") == players_win

    def test_decide_who_will_win_paper_scissor(self):
        assert decide_who_will_win("paper", "scissor") == computer_win

    def test_decide_who_will_win_scissor_scissor(self):
        assert decide_who_will_win("scissor", "scissor") == tie

    def test_decide_who_will_win_scissor_rock(self):
        assert decide_who_will_win("scissor", "rock") == computer_win

    def test_decide_who_will_win_scissor_paper(self):
        assert decide_who_will_win("scissor", "paper") == players_win


if __name__ == '__main__':
    unittest.main()
