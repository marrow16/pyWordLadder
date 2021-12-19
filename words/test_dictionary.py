import unittest

from words.dictionary import Dictionary
from words.word import Word

EXPECTED_DICTIONARY_SIZES: dict[int, int] = {
    2:  127,
    3:  1347,
    4:  5638,
    5:  12972,
    6:  23033,
    7:  34342,
    8:  42150,
    9:  42933,
    10: 37235,
    11: 29027,
    12: 21025,
    13: 14345,
    14: 9397,
    15: 5925
}


class DictionaryTestCase(unittest.TestCase):
    def test_can_construct_dictionary(self):
        dictionary = Dictionary(3)
        self.assertEqual(3, dictionary.word_length)
        self.assertEqual(1347, len(dictionary))

    def test_dictionary_sizes_correct(self):
        for word_len, expected_size in EXPECTED_DICTIONARY_SIZES.items():
            dictionary = Dictionary(word_len)
            self.assertEqual(word_len, dictionary.word_length)
            self.assertEqual(expected_size, len(dictionary))

    def test_invalid_word_length_dictionary_fails_to_load(self):
        with self.assertRaises(FileNotFoundError):
            Dictionary(1)
        with self.assertRaises(FileNotFoundError):
            Dictionary(16)

    def test_dictionary_word_has_linked_words(self):
        dictionary = Dictionary(3)
        word: Word = dictionary['cat']
        self.assertEqual(33, len(word.linked_words))
        self.assertFalse(word in word.linked_words)

    def test_dictionary_word_is_island_word(self):
        dictionary = Dictionary(3)
        word: Word = dictionary['iwi']
        self.assertTrue(word.is_island)
        self.assertEqual(0, len(word.linked_words))

    def test_differences_between_linked_words(self):
        dictionary = Dictionary(3)
        word: Word = dictionary['cat']
        self.assertTrue(len(word.linked_words) > 0)
        for linked_word in word.linked_words:
            self.assertEqual(1, word - linked_word)

    def test_words_are_inter_linked(self):
        dictionary = Dictionary(3)
        word: Word = dictionary['cat']
        self.assertTrue(len(word.linked_words) > 0)
        for linked_word in word.linked_words:
            self.assertTrue(word in linked_word)


if __name__ == '__main__':
    unittest.main()
