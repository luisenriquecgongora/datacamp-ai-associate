# Import needed functionality
from collections import Counter
from .utils import tokenize


# Define Document class
class Document:
    """A class for text analysis

    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    :ivar tokens: tokenized version of `text`, as a list of words
    :ivar word_counts: Counter containing counts of each token in `tokens`
    """
    def __init__(self, text):
        self.text = text
        # pre tokenize the document with non-public tokenize method
        self.tokens = self._tokenize()
        # pre tokenize the document with non-public count_words
        self.word_counts = self._count_words()

    def _tokenize(self):
        return tokenize(self.text)

    # non-public method to tally document's word counts with Counter
    def _count_words(self):
        return Counter(self.tokens)
