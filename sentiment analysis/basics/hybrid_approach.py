import nltk
nltk.download('afinn')
from nltk.sentiment.util import demo_afinn_sentiment
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load the training dataset
df = pd.read_csv('training_data.csv')

# Split the dataset into features (X) and labels (y)
X = df['text']
y = df['sentiment']

# Use CountVectorizer to convert the text data into a numerical feature matrix
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Tokenize the input text
tokens = nltk.word_tokenize(input_text)

# Calculate the overall sentiment score using the AFINN lexicon
afinn_score = demo_afinn_sentiment(tokens)

# If the AFINN score is 0, use the machine learning model to classify the sentiment
if afinn_score == 0:
    input_features = vectorizer.transform([input_text])
    prediction = model.predict(input_features)[0]
else:
    # Use the AFINN score as the overall sentiment
    if afinn_score > 0:
        prediction = 'positive'
    else:
        prediction = 'negative'
