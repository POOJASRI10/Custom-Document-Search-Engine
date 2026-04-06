import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    tokens = text.split()
    return tokens


def process_documents(documents):
    processed = {}

    for name, text in documents.items():
        processed[name] = preprocess(text)

    return processed