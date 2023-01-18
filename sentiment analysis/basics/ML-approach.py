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

# Predict the sentiment of new, unseen text
input_text = 'This movie was amazing!'
input_features = vectorizer.transform([input_text])
prediction = model.predict(input_features)[0]
