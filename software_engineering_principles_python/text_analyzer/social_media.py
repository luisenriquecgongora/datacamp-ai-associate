# Import needed functionality
from .document import Document
from .counter_utils import filter_word_counts
from .utils import tokenize

# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()

    def _tokenize(self):
        # Override Document's tokenizer so '#' and '@' symbols are kept
        return tokenize(self.text, regex=r'\S+')

    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, '#')

    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return filter_word_counts(self.word_counts, first_char='@')
