# Import needed package
import text_analyzer

# Sample multi-line tweet text, some lines are retweets
datacamp_tweets = (
    "RT @datacamp: Learn Data Science using Python and R with our online courses. #DataCamp #Python\n"
    "Just finished the Software Engineering track! #DataCamp #Python\n"
    "RT @datacamp: 5 amazing recent advances in AI you should know about #DataScience\n"
    "Excited for the next course on data visualization #DataViz\n"
)

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)

# Plot the most used hashtags in the retweets
text_analyzer.plot_counter(my_tweets.retweets.hashtag_counts)
