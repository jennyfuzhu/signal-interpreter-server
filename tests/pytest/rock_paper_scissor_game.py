# rock_paper_scissor_game.py, exercise 1
import pytest
# random will not work when we will do the unit testing
import random
from unittest.mock import patch

tie = "It was a tie"
players_win = "You won!"
computer_win = "You lost."
choices_list = ["rock", "paper", "scissor"]


class RandomClass:
    def decide_who_will_win(self,players_choice, computer_choice):
        """
        This function will take two input strings, one for the plaers´ choice and one for the computers´choice.
        It will return who the winner is.
        :param players_choice: the players´ choice, either rock, paper or scissor
        :param computer_choice: the computers´ choice, either, rock, paper or scissor
        :return: the winner or if it is a tie
        """
        # The computers choice
        # computer_choice = random.choice(choices_list)

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

    def play_game(self):
        """

        :return: a string of who is the winner or if it is a tie
        """
        # getting the player´s choice and save it to a variable "player_choice"
        player_choice = input("Enter your choice: ")
        # getting the computer´s choice
        computer_choice = self.get_robot_choice()
        # send above define variables to the function decide_who_will_win
        the_winner = self.decide_who_will_win(player_choice, computer_choice)
        # return the value for decide_who_will_win
        return the_winner

    # exercise 2a

    def get_robot_choice(self):
        """
        This function will return a random string from a list of choices
        :return:
        """
        # print out random choice by the robot
        robot_choice = random.choice(choices_list)
        print("Robots random choice: " + robot_choice)
        return robot_choice


if __name__ == "__main__":
    mod = RandomClass()
    mod.main()
