"""Word helpers."""


def word_count(text: str) -> int:
    """Number of whitespace separated words in `text`."""
    return len(text.split())


def title_case(text: str) -> str:
    """Capitalize the first letter of every word."""
    return " ".join(w[:1].upper() + w[1:] for w in text.split())


def slugify(text: str) -> str:
    """Lowercase URL slug: whitespace separated words joined by hyphens.

    Characters other than ASCII letters and digits are dropped; words left
    empty after that are skipped, so there are no leading, trailing or
    repeated hyphens.
    """
    words = ("".join(c for c in w.lower() if c.isascii() and c.isalnum()) for w in text.split())
    return "-".join(w for w in words if w)


def truncate_words(text: str, limit: int, ellipsis: str = "…") -> str:
    """Shorten `text` to at most `limit` whitespace separated words.

    Words are split as in `word_count`: any run of whitespace (spaces, tabs,
    newlines) is one separator, and leading and trailing whitespace is
    ignored. The kept words are always joined with a single space, whether or
    not anything was cut.

    `ellipsis` is appended directly to the last kept word, only when at least
    one word was cut; pass `ellipsis=" …"` for a space before it, or `""` to
    simply truncate. Empty or whitespace-only text gives `""`.

    A `limit` of 0 returns `""` with no ellipsis, whatever the text is. A
    negative `limit` raises `ValueError`, even for empty text.
    """
    if limit < 0:
        raise ValueError("limit must not be negative")
    if limit == 0:
        return ""
    words = text.split()
    if len(words) <= limit:
        return " ".join(words)
    return " ".join(words[:limit]) + ellipsis
