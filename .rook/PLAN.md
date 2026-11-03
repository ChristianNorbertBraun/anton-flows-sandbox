# Plan: add `truncate_words` to `textkit.words` (issue #10)

## Goal

Add `truncate_words(text: str, limit: int, ellipsis: str = "…") -> str` to
`textkit/words.py`. It shortens `text` to at most `limit` words and appends
`ellipsis` only when at least one word was cut.

## Decided behaviour (to be written into the docstring)

1. **Word definition and whitespace.** Words are whitespace separated, using
   `text.split()` with no argument. This matches `word_count`, `title_case` and
   `slugify`. Any run of whitespace (spaces, tabs, newlines) counts as one
   separator, and leading and trailing whitespace is ignored.
2. **Output is always normalized.** The kept words are joined with a single
   space, whether or not anything was cut. So `truncate_words("  a\tb  ", 5)`
   returns `"a b"`. This follows `title_case`, and the result does not depend
   on whether truncation happened.
3. **Ellipsis placement.** When words were cut, `ellipsis` is appended directly
   to the last kept word, with no space in between: `"a b c d", 2` gives
   `"a b…"`. If no word was cut (word count <= `limit`), no ellipsis is added.
   A caller who wants a space can pass `ellipsis=" …"`. `ellipsis=""` is
   allowed and simply truncates.
4. **`limit` of 0 or less.**
   - A negative `limit` raises `ValueError("limit must not be negative")`.
     The check runs before the text is looked at, so it raises even for
     empty text.
   - A `limit` of 0 returns `""` without an error and without an ellipsis,
     whatever the text is. This is an explicit exception to rule 3: a result
     made of only an ellipsis is not useful, so zero words means an empty
     string.
5. **Empty or whitespace-only text** (with a non-negative `limit`) returns
   `""` without an ellipsis, because nothing was cut.

## Implementation sketch

```python
def truncate_words(text: str, limit: int, ellipsis: str = "…") -> str:
    """<docstring documenting rules 1-5>"""
    if limit < 0:
        raise ValueError("limit must not be negative")
    if limit == 0:
        return ""
    words = text.split()
    if len(words) <= limit:
        return " ".join(words)
    return " ".join(words[:limit]) + ellipsis
```

## Files to change

- `textkit/words.py`: add the `truncate_words` function after `slugify`, with
  a docstring that states rules 1 to 5, in the style of `slugify`'s docstring.
- `tests/test_words.py`: import `truncate_words` and add one test per rule:
  - `test_truncate_words_cuts_and_appends_ellipsis`: `("one two three four", 2)` gives `"one two…"`.
  - `test_truncate_words_no_cut_no_ellipsis`: exactly `limit` words, and fewer than `limit` words, return no ellipsis.
  - `test_truncate_words_normalizes_whitespace`: tabs, newlines and repeated, leading or trailing spaces, both with and without a cut (for example `" a\n\tb  c ", 2` gives `"a b…"`, and `" a  b ", 5` gives `"a b"`).
  - `test_truncate_words_custom_ellipsis`: `ellipsis="..."`, `ellipsis=" …"` and `ellipsis=""`.
  - `test_truncate_words_empty_text`: `""` and `"   "` give `""`.
  - `test_truncate_words_zero_limit_returns_empty`: `limit` of `0` returns `""` with no error and no ellipsis, for non-empty text (`"a b c"`), for empty text, and with a custom `ellipsis`.
  - `test_truncate_words_negative_limit_raises`: `limit` of `-1` (and, for example, `-5`) raises `ValueError`, including with empty text.

No other files change. `textkit/__init__.py` does not re-export the existing
helpers, so it stays as it is.

## Out of scope

- Character-based truncation, or limits measured in characters.
- Keeping the original whitespace or punctuation layout of the input.
- Unicode word segmentation beyond `str.split()`.
- Changes to the existing helpers or to package exports.

## Verification

- Run `python3 -m unittest discover -s tests`. All existing and new tests must pass.
- Check that the diff touches only `textkit/words.py` and `tests/test_words.py`, and uses only the standard library.
