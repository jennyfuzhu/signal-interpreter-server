import pytest
# random will not work when we will do the unit testing
from random import random

tie = "It was a tie"
players_win = "You won!"
computer_win = "You lost."


def decide_who_will_win(players_choice, computer_choice):
    # List of possible choices
    #choices_list = ["rock", "paper", "scissor"]
    # The computers choice
    #computer_choice = random.choice(choices_list)

    if players_choice == computer_choice:
        return tie
    elif players_choice == "rock":
        if computer_choice == "scissor":
            return players_win
        else:
            return computer_win
    elif players_choice == "paper":
        if computer_choice == "rock":
            return players_win
        else:
            return computer_win
    elif players_choice == "scissor":
        if computer_choice == "paper":
            return players_win
        else:
            return computer_win

def test_decide_who_will_win():
    assert decide_who_will_win("rock", "rock") == tie
    assert decide_who_will_win("rock", "paper") == computer_win
    assert decide_who_will_win("rock", "scissor") == players_win
    assert decide_who_will_win("paper", "paper") == tie
    assert decide_who_will_win("paper", "rock") == players_win
    assert decide_who_will_win("paper", "scissor") == computer_win
    assert decide_who_will_win("scissor", "scissor") == tie
    assert decide_who_will_win("scissor", "rock") == computer_win
    assert decide_who_will_win("scissor", "paper") == players_win
