import unittest

from textkit.words import title_case, word_count


class WordsTest(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(word_count("a b  c"), 3)
        self.assertEqual(word_count(""), 0)

    def test_title_case(self):
        self.assertEqual(title_case("hello big world"), "Hello Big World")


if __name__ == "__main__":
    unittest.main()
