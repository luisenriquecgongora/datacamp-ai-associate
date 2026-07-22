# Import local package
import text_analyzer

# Sample tweet text
datacamp_tweet = (
    "Learn Data Science using Python and R with our online courses. "
    "Start today with a free trial! #DataCamp #Python #DataScience @Luis"
)

# create a new document instance from datacamp_tweets
datacamp_doc = text_analyzer.Document(text=datacamp_tweet)

# print the first 5 tokens from datacamp_doc
print(datacamp_doc.tokens[:5])

# print the top 5 most used words in datacamp_doc
print(datacamp_doc.word_counts.most_common(5))
