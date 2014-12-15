import random
random.seed()
randint = random.randint

def roll2d6():
    """Returns a tuple containing the results of the two d6 rolls"""
    return (randint(1,6), randint(1,6))
