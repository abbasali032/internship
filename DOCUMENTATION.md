DOCUMENTATION:

Step 1: Import the TextBlob Class
```python
from textblob import TextBlob
```
This line imports the `TextBlob` class from the `textblob` library. It allows us to use the functionality provided by TextBlob for text processing and analysis.

Step 2: Define Sample Text
```python
text = "food is absolutely wonderful"
```
Here, we define a sample text string that we want to analyze for sentiment. In this case, the text is "food is absolutely wonderful".

Step 3: Create a TextBlob Object
```python
blob = TextBlob(text)
```
This line creates a `TextBlob` object named `blob` from the sample text. The `TextBlob` object represents the textual data and provides methods to perform various operations like sentiment analysis, part-of-speech tagging, noun phrase extraction, etc.

Step 4: Perform Sentiment Analysis
```python
sentiment = blob.sentiment
```
This line calculates the sentiment of the text using the `sentiment` property of the `TextBlob` object. The `sentiment` property returns a named tuple containing two values: polarity and subjectivity. Polarity indicates the sentiment's positivity or negativity, while subjectivity indicates how subjective or opinionated the text is.

Step 5: Print Sentiment Scores
```python
print("Polarity: ", sentiment.polarity)
print("Subjectivity: ", sentiment.subjectivity)
```
These lines print out the polarity and subjectivity scores of the text. The polarity score ranges from -1 to 1, where negative values indicate negative sentiment, positive values indicate positive sentiment, and 0 indicates neutral sentiment. The subjectivity score ranges from 0 to 1, where 0 indicates objective and 1 indicates subjective.

Step 6: Determine Overall Sentiment
```python
if sentiment.polarity > 0:
    print("The text is positive.")
elif sentiment.polarity < 0:
    print("The text is negative.")
else:
    print("The text is neutral.")
```
These lines determine the overall sentiment of the text based on its polarity score. If the polarity score is greater than 0, the text is considered positive. If the polarity score is less than 0, the text is considered negative. If the polarity score is exactly 0, the text is considered neutral.

By following these steps, you can analyze the sentiment of text using TextBlob in Python. Each step contributes to loading the text, analyzing its sentiment, and presenting the results.

OUTPUT:
The text is positive.


        
