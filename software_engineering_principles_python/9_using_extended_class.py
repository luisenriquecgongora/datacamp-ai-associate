# Import local package
import text_analyzer

# Sample tweet text
# Sample tweet text
datacamp_tweet = (
    "Learn Data Science using Python and R with our online courses. "
    "Start today with a free trial! #DataCamp #Python #DataScience @Luis"
)

# Create a SocialMedia instance with datacamp_tweets
dc_tweets = text_analyzer.SocialMedia(text=datacamp_tweet)

# Print the top five most mentioned users
print(dc_tweets.hashtag_counts.most_common(5))

# Plot the most used hashtags
text_analyzer.plot_counter(dc_tweets.hashtag_counts)