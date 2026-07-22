# Import local package
import text_analyzer

# Sample tweet text
datacamp_tweet = (
    "Learn Data Science using Python and R with our online courses. "
    "Start today with a free trial! #DataCamp #Python #DataScience"
)

# Create an instance of Document with datacamp_tweet
my_document = text_analyzer.Document(text=datacamp_tweet)

# Print the text attribute of the Document instance
print(my_document.text)
