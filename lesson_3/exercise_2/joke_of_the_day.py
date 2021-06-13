def joke_of_the_day():
    print("---Joke of the day---")
    answer = input("What do you call a man with a rubber toe?")
    if 'duck' in answer.lower():
        print("Correct!")
    else:
        print("Wrong answer! The correct answer is 'Duck!'")


if __name__ == "__main__":
    joke_of_the_day()
