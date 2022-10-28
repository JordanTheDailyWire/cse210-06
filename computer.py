# Import choice and objects
from random import choice
from objects import Paper, Rock, Scissors

class Computer():
    def __init__(self):
        pass
    def get_guess(self):
        text = choice(['r','s','p'])
        if text == 'p':
            return Paper()
        elif text == 'r':
            return Rock()
        elif text == 's':
            return Scissors()
        else:
            raise Exception("This should not be able to happen")