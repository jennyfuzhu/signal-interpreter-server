def practice_capitals():
    # ask the user to enter a country
    capital_input = input("Enter a country: ")
    # call the get_capital function with the
    # country as input param
    # and save the return value into a variable called capital
    try:
        capital = get_capital(capital_input)

        # print out the capital citu of the countru in the following format
        # The capital of X is Y
        # where X is the country enetered by he user
        # and Y is the caputal city we got from the
        # get_capital function
        print("The capital of %s is %s" + capital_input + capital)
    except KeyError:

        # if the get_capital function raises a key error, the practice
        # capitals function should instead print out the
        # country X does not exist in our dictionary
        # where X is the country the user entered

        print("The country %s X does not exist in our dictionary")


def get_capital(country):
    # return a country
    dictionary = {"Sweden": "Stockholm",
                  "Norway": "Oslo",
                  "England": "London"
                  }

    return dictionary[country]
