# Import needed functionality
from re import findall


def tokenize(text, regex=r'[a-zA-Z]+'):
    """Split text into a list of tokens using the given regex."""
    return findall(regex, text)


def filter_lines(lines, first_chars):
    """Filter lines to only retain those that start with `first_chars`."""
    return '\n'.join(
        [line for line in lines.split('\n') if line.startswith(first_chars)]
    )
