# game.py
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methodsre  

# import pdb; pdb.set_trace()
import random
import string
import requests
# import collections
# collections.Callable = collections.abc.Callable

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
        return self.__check_dictionary(word)
    
    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}", verify=False)
        json_response = response.json()
        return json_response['found']

# g = Game()
# print(g.is_valid(""))