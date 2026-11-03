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
