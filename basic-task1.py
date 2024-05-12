from textblob import TextBlob

# Sample text
text = "food is absolutly wonderful"

# Create a TextBlob object
blob = TextBlob(text)

# Perform sentiment analysis
sentiment = blob.sentiment

# Output the sentiment
print("Polarity: ", sentiment.polarity)  # [-1.0, 1.0], where 1 means positive sentiment
print("Subjectivity: ", sentiment.subjectivity)  # [0.0, 1.0], where 1 means very subjective

# Determine overall sentiment
if sentiment.polarity > 0:
    print("The text is positive.")
elif sentiment.polarity < 0:
    print("The text is negative.")
else:
    print("The text is neutral.")