import unittest

from solving.puzzle import Puzzle
from words.dictionary import Dictionary


class PuzzleTestCase(unittest.TestCase):
    def test_calculate_minimum_ladder_length_no_diff(self):
        dictionary = Dictionary(3)
        cat = dictionary['cat']
        puzzle = Puzzle(cat, cat)
        self.assertEqual(1, puzzle.calculate_minimum_ladder_length())

    def test_calculate_minimum_ladder_length_1_diff(self):
        dictionary = Dictionary(3)
        cat = dictionary['cat']
        cot = dictionary['cot']
        puzzle = Puzzle(cat, cot)
        self.assertEqual(2, puzzle.calculate_minimum_ladder_length())

    def test_calculate_minimum_ladder_length_2_diff(self):
        dictionary = Dictionary(3)
        cat = dictionary['cat']
        bar = dictionary['bar']
        puzzle = Puzzle(cat, bar)
        self.assertEqual(3, puzzle.calculate_minimum_ladder_length())

    def test_calculate_minimum_ladder_length_all_diff(self):
        dictionary = Dictionary(3)
        cat = dictionary['cat']
        dog = dictionary['dog']
        puzzle = Puzzle(cat, dog)
        self.assertEqual(4, puzzle.calculate_minimum_ladder_length())

    def test_calculate_minimum_ladder_length_longest(self):
        dictionary = Dictionary(3)
        exo = dictionary['exo']
        zzz = dictionary['zzz']
        puzzle = Puzzle(exo, zzz)
        self.assertEqual(9, puzzle.calculate_minimum_ladder_length())

if __name__ == '__main__':
    unittest.main()
