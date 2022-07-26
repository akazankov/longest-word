# game.py
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

# import pdb; pdb.set_trace()
import random
import string

class Game:
    def __init__(self):
        self.grid = random.choices(string.ascii_uppercase, k = 9)

    def is_valid(self, word):
        if not word:
            return False
        # letters = self.grid.copy()
        # for letter in word:
        #     if letter in letters:
        #         letters.remove(letter)
        #     else:
        #         return False
        # return True
        for letter in list(word):
            if letter not in self.grid:
                return False
        return True
