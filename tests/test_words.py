import unittest

from textkit.words import slugify, title_case, truncate_words, word_count


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

    def test_truncate_words_cuts_and_appends_ellipsis(self):
        self.assertEqual(truncate_words("one two three four", 2), "one two…")

    def test_truncate_words_no_cut_no_ellipsis(self):
        self.assertEqual(truncate_words("one two three", 3), "one two three")
        self.assertEqual(truncate_words("one two", 5), "one two")

    def test_truncate_words_normalizes_whitespace(self):
        self.assertEqual(truncate_words(" a\n\tb  c ", 2), "a b…")
        self.assertEqual(truncate_words(" a  b ", 5), "a b")
        self.assertEqual(truncate_words("a\tb", 2), "a b")

    def test_truncate_words_custom_ellipsis(self):
        self.assertEqual(truncate_words("a b c", 2, ellipsis="..."), "a b...")
        self.assertEqual(truncate_words("a b c", 2, ellipsis=" …"), "a b …")
        self.assertEqual(truncate_words("a b c", 2, ellipsis=""), "a b")
        self.assertEqual(truncate_words("a b", 2, ellipsis="..."), "a b")

    def test_truncate_words_empty_text(self):
        self.assertEqual(truncate_words("", 3), "")
        self.assertEqual(truncate_words("   ", 3), "")

    def test_truncate_words_zero_limit_returns_empty(self):
        self.assertEqual(truncate_words("a b c", 0), "")
        self.assertEqual(truncate_words("", 0), "")
        self.assertEqual(truncate_words("a b c", 0, ellipsis="..."), "")

    def test_truncate_words_negative_limit_raises(self):
        for limit in (-1, -5):
            with self.assertRaises(ValueError):
                truncate_words("a b c", limit)
            with self.assertRaises(ValueError):
                truncate_words("", limit)


if __name__ == "__main__":
    unittest.main()
