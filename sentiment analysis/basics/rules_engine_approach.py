def get_sentiment(text):
    if 'love' in text.lower():
        return 'positive'
    elif 'hate' in text.lower():
        return 'negative'
    else:
        return 'neutral'

input_text = 'I love this movie!'
sentiment = get_sentiment(input_text)
