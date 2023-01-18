import spacy
nlp = spacy.load('en_core_web_md')

# Tokenize the input text and perform part-of-speech tagging
doc = nlp(input_text)

# Iterate over the tokens and calculate the sentiment of each token based on its part-of-speech tag
sentiment_score = 0
for token in doc:
    if token.pos_ in ['ADJ', 'VERB']:
        if token.lemma_ in positive_words:
            sentiment_score += 1
        elif token.lemma_ in negative_words:
            sentiment_score -= 1

# Calculate the overall sentiment of the text
if sentiment_score > 0:
    sentiment = 'positive'
elif sentiment_score < 0:
    sentiment = 'negative'
else:
    sentiment = 'neutral'
