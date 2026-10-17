"""Word helpers."""


def word_count(text: str) -> int:
    """Number of whitespace separated words in `text`."""
    return len(text.split())


def title_case(text: str) -> str:
    """Capitalize the first letter of every word."""
    return " ".join(w[:1].upper() + w[1:] for w in text.split())
