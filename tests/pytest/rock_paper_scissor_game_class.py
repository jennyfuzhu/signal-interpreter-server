import random

choices_list = ["rock", "paper", "scissor"]


class RandomClass:
    def get_robot_choice_from_random(self):
        robot_choice = random.choice(choices_list)
        return robot_choice


def get_robot_choice():
    # print out random choice by the robot
    random_class = RandomClass()
    robot_choice = random_class.get_robot_choice_from_random()
    print("Robots random choice: " + robot_choice)
    return robot_choice


