# Import needed functionality
from collections import Counter
from .document import Document
import matplotlib.pyplot as plt
import doctest

def plot_counter_most_common(top_items):
  # Unpack the (word, count) pairs and plot them as a bar chart
  words, counts = zip(*top_items)
  plt.bar(words, counts)
  plt.xlabel('Word')
  plt.ylabel('Count')
  plt.show()

def plot_counter(counter, n_most_common=5):
  # Subset the n_most_common items from the input counter
  top_items = counter.most_common(n_most_common)
  # Plot `top_items`
  plot_counter_most_common(top_items)

def sum_counters(counters):
  """Aggregate collections.Counter objects by summing counts
  :param counters: list/tuple of counters to sum
  :return: aggregated counters with counts summed
  >>> d1 = Document('1 2 fizz 4 buzz fizz 7 8')
  >>> d2 = Document('fizz buzz 11 fizz 13 14')
  >>> sum_counters([d1.word_counts, d2.word_counts])
  Counter({'fizz': 4, 'buzz': 2})
  """
  return sum(counters, Counter())

doctest.testmod()

def filter_word_counts(word_counts, first_char):
  # Filter a Counter object on whether items start with `first_char`
  return Counter(
    {word: count for word, count in word_counts.items() if word.startswith(first_char)}
  )