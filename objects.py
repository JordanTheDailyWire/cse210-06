# Import Guess
from guess import Guess

# The object known as paper that the guesser and computer are choosing in the game
# Paper always beats the Rock in an instance
class Paper(Guess):
    def __init__(self):
        pass
    def beats(self, guess):
        if isinstance(guess, Rock):
            return True
        return False

# The object known as Sissors that the guesser and computer are choosing in the game
# Scissors always beats the Paper in an instance
class Scissors(Guess):
    def __init__(self):
        pass
    def beats(self, guess):
        if isinstance(guess, Paper):
            return True
        return False

# The object known as Rock that the guesser and computer are choosing in the game
# Rock always beats the Scissors in an instance
class Rock(Guess):
    def __init__(self):
        pass
    def beats(self, guess):
        if isinstance(guess, Scissors):
            return True
        return False