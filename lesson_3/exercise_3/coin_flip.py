import random


def get_three_heads():
    nmb_of_heads = 0
    nmb_of_tries = 0
    while nmb_of_heads < 3:
        # loop until three heads
        head_tail = random.choice(["heads", "tails"])
        print("Got " + head_tail)
        if head_tail == "heads":
            nmb_of_heads += 1
        nmb_of_tries += 1
    print("Number of tries until three heads: " + nmb_of_heads)


if __name__ == "__main__":
    get_three_heads()
