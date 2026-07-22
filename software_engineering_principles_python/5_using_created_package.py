# Import local package
import text_analyzer
from collections import Counter

# Sample word_counts: a list of Counter objects, one per "document"
word_counts = [
    Counter("the quick brown fox jumps over the lazy dog".split()),
    Counter("the dog barks at the fox in the brown field".split()),
    Counter("a quick fox runs quickly through the quiet field".split()),
]

# Sum word_counts using sum_counters from text_analyzer
word_count_totals = text_analyzer.sum_counters(word_counts)
print(word_count_totals)

# Plot word_count_totals using plot_counter from text_analyzer
text_analyzer.plot_counter(word_count_totals)
