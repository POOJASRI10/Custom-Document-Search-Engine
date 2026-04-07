## Custom Semantic Document Search Engine

## Overview

This project implements a custom semantic document search engine using manual TF-IDF vectorization and cosine similarity
The system takes a user query and returns the top 3 most relevant documents from a corpus of text files.
No external NLP libraries or pretrained models are used. All logic is implemented from scratch using basic Python.

## Features

- Manual TF-IDF implementation
- Cosine similarity for ranking
- FastAPI backend
- REST API endpoint for search
- Minimal frontend UI (HTML + JS)
- Clean and modular code structure

## Project Structure 

```
Spritle/
│
├── api.py        # FastAPI backend
├── loader.py     # Load documents
├── preprocess.py # Text preprocessing
├── vectorizer.py # TF-IDF logic
├── main.py       
│
├── documents/    # Input text files (Given 50 documents)
│
├── static/
│ └── index.html  # Simple Frontend UI
│
└── README.md     #contains the project details
```

## Setup Instructions

1. Clone or download the project
git clone (https://github.com/POOJASRI10/Custom-Document-Search-Engine)
cd Spritle

2. Install dependencies
pip install fastapi uvicorn

3. Run the backend server
uvicorn api:app --reload

4. Access the application
UI: http://127.0.0.1:8000

API Docs (Swagger): http://127.0.0.1:8000/docs

API Usage
End

GET /search?q=<query>

 Sample API Call

http://127.0.0.1:8000/search?q=artificial intelligence in finance


## Example Response

```json
{
  "results": [
    {
      "document": "doc_02_ai_in_finance.txt",
      "score": 0.3091,
      "snippet": "AI in Finance: Transforming the Landscape of Financial Services..."
    },
    {
      "document": "doc_51_ai_for_financial_forecasting.txt",
      "score": 0.1137,
      "snippet": "The integration of Artificial Intelligence into financial forecasting..."
    },
    {
      "document": "doc_22_ai_and_data_privacy.txt",
      "score": 0.1119,
      "snippet": "AI and Data Privacy: Navigating the Intersection of Innovation..."
    }
  ]
}


Methologies

1. Text Preprocessing

- Lowercasing
- Removing punctuation
- Tokenization

2. TF-IDF Vectorization (Manual)

- Term Frequency (TF):
TF = (word count in document) / (total words in document)

- Inverse Document Frequency (IDF):
IDF = log((N + 1) / (doc_count + 1)) + 1

TF-IDF: TF-IDF = TF × IDF

3. Similarity Computation

Cosine similarity is used to measure similarity between query and document vectors:
cos(θ) = (A · B) / (|A| |B|)

Constraints Followed

- No external NLP libraries used (e.g., sklearn, spacy, gensim)
- No pretrained embeddings or APIs
- Only Python standard libraries used (math, re, os)
- Future Improvements (Optional)
- Synonym handling for better semantic matching
- Performance optimization using vector libraries
- Advanced UI enhancements
- Stopword removal


Future Improvements

- Synonym handling for better semantic matching
- Performance optimization
- Advanced UI enhancements

Working

The search engine follows a multi-stage pipeline to process documents and retrieve the most relevant results for a given query.

1. Document Loading

- All text files are read from the `/documents/` directory.
- Each document is stored as raw text.
- The system maintains a mapping between document names and their content.

2. Text Preprocessing

Each document undergoes preprocessing to normalize the text:

- Convert text to lowercase
- Remove punctuation and special characters
- Tokenize text into individual words

This ensures consistent comparison between documents and queries.

3. Vocabulary Construction

- A global vocabulary is created using all unique words across all documents.
- This vocabulary forms the basis for vector representation.
- Each word corresponds to a specific index in the vector space.

4. TF (Term Frequency) Computation

For each document:

- Count how many times each word appears
- Normalize by total number of words in the document

Formula: TF = (count of word in document) / (total words in document)

5. IDF (Inverse Document Frequency) Computation

- Measures how important a word is across all documents
- Words that appear in many documents get lower weight

Formula: 5. IDF (Inverse Document Frequency) Computation

- Measures how important a word is across all documents
- Words that appear in many documents get lower weight

Formula: IDF = log((N + 1) / (doc_count + 1)) + 1


Where:
- N = total number of documents
- doc_count = number of documents containing the word

6. TF-IDF Vector Construction

- Each document is converted into a numerical vector
- Each value represents the importance of a word in that document
  TF-IDF = TF × IDF

7. Query Processing

When a user enters a query:

- The query is preprocessed using the same steps as documents
- It is converted into a TF-IDF vector using the same vocabulary

8. Similarity Computation

- The query vector is compared with all document vectors
- Cosine similarity is used to measure relevance
  cos(θ) = (A · B) / (|A| |B|)
- Higher value → more similar document

9. Ranking and Retrieval

- All documents are ranked based on similarity score
- Top 3 most relevant documents are selected

10. Result Generation

For each selected document, the system returns:

- Document name
- Similarity score
- A short snippet (first 200 characters)

Summary

The system transforms raw text into numerical vectors and uses mathematical similarity to retrieve relevant documents. It relies entirely on classical information retrieval techniques implemented from scratch without external NLP libraries.

Author
Poojasri@2026
=======
# Custom-Document-Search-Engine
Custom semantic document search engine using manual TF-IDF and cosine similarity with a FastAPI backend and interactive UI.
>>>>>>> e2b56742bac9d5547c7f27c869a52af3ba4702d6
