from rock_paper_scissor_game import RandomClass
from unittest.mock import patch


@patch.object(RandomClass, "rock_paper_scissor_game.random"
                           ".choice")
def test_get_robot_choice(mock_choice):
    the_class = RandomClass()
    mock_choice.return_value = "scissor"
    assert the_class.get_robot_choice() == "scissor"
