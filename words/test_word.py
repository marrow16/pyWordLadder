import unittest

from words.word import Word


class WordTestCase(unittest.TestCase):
    def test_can_construct_word(self):
        word = Word('cat')
        self.assertEqual('CAT', word.actual_word)
        self.assertEqual('CAT', str(word))

    def test_word_variations_are_correct(self):
        word = Word('cat')
        variations = word.variations
        self.assertEqual(3, len(variations))
        self.assertEqual('_AT', variations[0])
        self.assertEqual('C_T', variations[1])
        self.assertEqual('CA_', variations[2])

    def test_word_differences_are_correct(self):
        cat = Word('cat')
        cot = Word('cot')
        dog = Word('dog')
        self.assertEqual(0, cat - cat)
        self.assertEqual(0, cot - cot)
        self.assertEqual(0, dog - dog)
        self.assertEqual(1, cat - cot)
        self.assertEqual(1, cot - cat)
        self.assertEqual(2, cot - dog)
        self.assertEqual(2, dog - cot)
        self.assertEqual(3, cat - dog)
        self.assertEqual(3, dog - cat)


if __name__ == '__main__':
    unittest.main()
