import unittest

from textkit.words import slugify, title_case, word_count


class WordsTest(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(word_count("a b  c"), 3)
        self.assertEqual(word_count(""), 0)

    def test_title_case(self):
        self.assertEqual(title_case("hello big world"), "Hello Big World")

    def test_slugify(self):
        self.assertEqual(slugify("Hello, Big World!"), "hello-big-world")

    def test_slugify_empty(self):
        self.assertEqual(slugify(""), "")

    def test_slugify_only_punctuation(self):
        self.assertEqual(slugify("!?, ... --"), "")

    def test_slugify_drops_non_ascii_and_extra_space(self):
        self.assertEqual(slugify("  Café  Nº 5 - ok "), "caf-n-5-ok")


if __name__ == "__main__":
    unittest.main()
