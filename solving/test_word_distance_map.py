import unittest

from solving.word_distance_map import WordDistanceMap
from words.dictionary import Dictionary


class WordDistanceMapTestCase(unittest.TestCase):
    def test_island_word_has_limited_map(self):
        dictionary: Dictionary = Dictionary(3)
        word = dictionary['iwi']
        wdm = WordDistanceMap(word, None)
        self.assertEqual(1, len(wdm))
        self.assertEqual(1, wdm[word])
        self.assertTrue(word in wdm)
        self.assertTrue(wdm.reachable(word, 1))
        self.assertFalse(wdm.reachable(word, 0))

        self.assertFalse(dictionary['cat'] in wdm)

    def test_cat_map(self):
        dictionary: Dictionary = Dictionary(3)
        word = dictionary['cat']
        wdm = WordDistanceMap(word, None)

        self.assertEqual(1346, len(wdm))
        self.assertEqual(1, wdm[word])

        end_word = dictionary['dog']
        self.assertTrue(end_word in wdm)
        self.assertEqual(4, wdm[end_word])
        self.assertTrue(wdm.reachable(end_word, 5))
        self.assertTrue(wdm.reachable(end_word, 4))
        self.assertFalse(wdm.reachable(end_word, 3))
        self.assertFalse(wdm.reachable(end_word, 2))
        self.assertFalse(wdm.reachable(end_word, 1))
        self.assertFalse(wdm.reachable(end_word, 0))

    def test_cat_map_limited(self):
        dictionary: Dictionary = Dictionary(3)
        word = dictionary['cat']
        wdm = WordDistanceMap(word, 4)
        self.assertEqual(1086, len(wdm))

        end_word = dictionary['dog']
        self.assertTrue(end_word in wdm)
        self.assertTrue(wdm.reachable(end_word, 5))
        self.assertTrue(wdm.reachable(end_word, 4))
        self.assertFalse(wdm.reachable(end_word, 3))
        self.assertFalse(wdm.reachable(end_word, 2))

        # limit further...
        wdm = WordDistanceMap(word, 3)
        self.assertEqual(345, len(wdm))
        self.assertFalse(end_word in wdm)

if __name__ == '__main__':
    unittest.main()
