# tests/test_game.py
import unittest
import string
from game import Game
import collections
collections.Callable = collections.abc.Callable

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)
            
    def test_empty_word_is_invalid(self):
        new_game = Game()
        # self.assertIs(new_game.is_valid(''), False)
        self.assertFalse(new_game.is_valid(''))

    def test_is_valid(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ') # Force the grid to a test case:
        # self.assertIs(new_game.is_valid('EUREKA'), True)
        self.assertTrue(new_game.is_valid('EUREKA'))
        self.assertEqual(new_game.grid, list('KWEUEAKRZ')) # Make sure the grid remained untouched

    def test_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ') # Force the grid to a test case:
        # self.assertIs(new_game.is_valid('SANDWICH'), False)
        self.assertFalse(new_game.is_valid('SANDWICH'))
        self.assertEqual(new_game.grid, list('KWEUEAKRZ')) # Make sure the grid remained untouched
    
    def test_unknown_word_is_invalid(self):
      new_game = Game()
      new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
      self.assertFalse(new_game.is_valid('FEUN'))
    #   self.assertIs(new_game.is_valid('FEUN'), False)
