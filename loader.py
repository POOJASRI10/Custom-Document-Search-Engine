import os

def load_documents(path):
    documents = {}

    for filename in os.listdir(path):
        if filename.endswith(".txt"):
            with open(os.path.join(path, filename), "r", encoding="utf-8") as f:
                documents[filename] = f.read()

    return documents