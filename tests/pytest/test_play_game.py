from tests.pytest.rock_paper_scissor_game import RandomClass
from unittest.mock import patch

"""Instructions: Do not forget to mock the input-function as well as the get_robot_choice-function and 
decide_who_will_win-function so it becomes a pure unit test. Remember that if you use a decorator, the parameter 
order will be “reversed”. """

tie = "It was a tie"
players_win = "You won!"
computer_win = "You lost."

# instance of the class
the_class = RandomClass()


@patch("builtins.input")
@patch("tests.pytest.rock_paper_scissor_game.get_robot_choice")
@patch("tests.pytest.rock_paper_scissor_game.decide_who_will_win")
def test_play_game(mock_input, mock_get_robot_choice, mock_decide_who_will_win):
    mock_input.return_value = "rock"
    mock_get_robot_choice.return_value = "scissor"
    mock_decide_who_will_win.return_value = players_win
    assert play_game() == players_win
