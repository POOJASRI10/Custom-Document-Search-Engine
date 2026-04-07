## Custom Semantic Document Search Engine

## Basic Understanding of the Problem Statement

The goal of this project is to build a Custom Semantic Document Search Engine that retrieves the most relevant documents for a given user query, without relying on any external AI or NLP libraries.

Unlike traditional keyword-based search systems, this project focuses on understanding the importance of words within documents using mathematical techniques. The system processes a collection of text files, converts them into numerical representations using TF-IDF (Term Frequency–Inverse Document Frequency), and compares them with the user query using cosine similarity.

The key challenge lies in implementing all components manually, including text preprocessing, vectorization, and similarity computation, using only basic Python libraries. This ensures a deep understanding of how search engines work internally, without abstracting the logic through prebuilt tools.

The final system accepts a query, evaluates its similarity against all documents in the dataset, and returns the Top 3 most relevant results, along with their scores and meaningful text snippets.

## Overview

This project implements a **Custom Semantic Document Search Engine** using **manual TF-IDF vectorization and cosine similarity**.

The system takes a user query and returns **The top 3 most relevant documents** from a corpus of text files.

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

1. **Clone or download the project**

     ```git clone https://github.com/POOJASRI10/Custom-Document-Search-Engine ```

     ```cd Spritle```

3. **Install dependencies**

   ```pip install fastapi uvicorn```

5. **Run the backend server**

   ```uvicorn api:app --reload```

## Usage

**1. Access the Application**

- **UI (Frontend):**  

  http://127.0.0.1:8000  

- **API Documentation (Swagger):**  

  http://127.0.0.1:8000/docs  

**2. API Endpoint**
   
    GET /search?q=<query>
    
**3. Example API Call**
    
     http://127.0.0.1:8000/search?q=artificial%20intelligence%20in%20finance

**4. Description**

- The `/search` endpoint accepts a query string.
- It returns the **top 3 most relevant documents** based on TF-IDF and cosine similarity.
- Each result includes:
  - Document name  
  - Similarity score  
  - Text snippet  

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
```
## Methologies

1. **Text Preprocessing**

- Lowercasing
- Removing punctuation
- Tokenization

2. **TF-IDF Vectorization** (Manual)

    ```TF-IDF: TF-IDF = TF × IDF```
   
- Term Frequency (TF):

  ```TF = (word count in document) / (total words in document)```

- Inverse Document Frequency (IDF):

  ```IDF = log((N + 1) / (doc_count + 1)) + 1```

3. **Similarity Computation**

     Cosine similarity is used to measure similarity between query and document vectors:
  
      ```cos(θ) = (A · B) / (|A| |B|)```

 ## Constraints Followed

- No external NLP libraries used (e.g., sklearn, spacy, gensim)
- No pretrained embeddings or APIs
- Only Python standard libraries used (math, re, os)
- Future Improvements (Optional)
- Synonym handling for better semantic matching
- Performance optimization using vector libraries
- Advanced UI enhancements
- Stopword removal


## Future Improvements

- Synonym handling for better semantic matching
- Performance optimization
- Advanced UI enhancements

## Model Working

   The search engine follows a multi-stage pipeline to process documents and retrieve the most relevant results for a given query.

1. **Document Loading**

- All text files are read from the `/documents/` directory.
- Each document is stored as raw text.
- The system maintains a mapping between document names and their content.

2. **Text Preprocessing**

     Each document undergoes preprocessing to normalize the text:

- Convert text to lowercase
- Remove punctuation and special characters
- Tokenize text into individual words

     This ensures consistent comparison between documents and queries.

3. **Vocabulary Construction**

- A global vocabulary is created using all unique words across all documents.
- This vocabulary forms the basis for vector representation.
- Each word corresponds to a specific index in the vector space.

4. **TF (Term Frequency) Computation**

     For each document:

- Count how many times each word appears
- Normalize by the total number of words in the document

   ```TF = (count of word in document) / (total words in document)```

5. **IDF (Inverse Document Frequency) Computation**

- Measures how important a word is across all documents
- Words that appear in many documents get a lower weight

  ```IDF = log((N + 1) / (doc_count + 1)) + 1```

   Where:
- N = total number of documents
- doc_count = number of documents containing the word

6. **TF-IDF Vector Construction**

- Each document is converted into a numerical vector
- Each value represents the importance of a word in that document
  Formula: TF-IDF = TF × IDF

7. **Query Processing**

      When a user enters a query:
   
- The query is preprocessed using the same steps as documents
- It is converted into a TF-IDF vector using the same vocabulary

8. **Similarity Computation**

- The query vector is compared with all document vectors
- Cosine similarity is used to measure relevance

   ```cos(θ) = (A · B) / (|A| |B|)```

- Higher value → more similar document

9. **Ranking and Retrieval**

- All documents are ranked based on similarity score
- Top 3 most relevant documents are selected

10. **Result Generation**

     For each selected document, the system returns:
- Document name
- Similarity score
- A short snippet (first 200 characters)


## Challenges Faced and Solutions

### 1. Implementing TF-IDF from Scratch

**Challenge:**  
Understanding how to correctly compute TF, IDF, and combine them without using libraries like sklearn was initially confusing. Handling edge cases like division by zero and ensuring correct normalization required careful implementation.

**Solution:**  
Broke the problem into smaller parts:
- Implemented TF first
- Then IDF separately
- Finally combined them into TF-IDF  
Also used a smoothed IDF formula:

IDF = log((N + 1) / (doc_count + 1)) + 1

This improved stability and avoided zero values.

### 2. Handling Query and Document Consistency

**Challenge:**  
The query and documents must be processed in the same way. Initially, mismatches in preprocessing caused poor or incorrect results.

**Solution:**  
Created a common preprocessing function and reused it for both documents and queries. This ensured consistent tokenization and improved accuracy.

### 3. Low Accuracy for Short Queries

**Challenge:**  
Queries like "AI in finance" sometimes returned weaker results because the system does not understand synonyms (e.g., "AI" vs "artificial intelligence").

**Solution:**  
Improved query handling by:
- Encouraging full-term queries
- Cleaning and normalizing text  
Recognized this as a limitation of TF-IDF-based systems.

### 4. UI Not Displaying Results Properly

**Challenge:**  
Initially, the frontend UI had issues:
- Query with spaces was not working correctly
- Special characters like `**` appeared in snippets

**Solution:**  
- Used `encodeURIComponent()` to properly send queries  
- Cleaned snippet text in backend using:
  - Removing `**`
  - Removing newline characters  

## Key Learnings

- Deep understanding of TF-IDF and cosine similarity
- Importance of consistent preprocessing
- Handling real-world debugging (API, UI, Git)
- Writing clean and structured documentation

## UI SCREENSHOT

<img width="990" height="814" alt="image" src="https://github.com/user-attachments/assets/03930330-bdaa-46d5-820c-efd0903acc43" />

## Summary

The system transforms raw text into numerical vectors and uses mathematical similarity to retrieve relevant documents. It relies entirely on classical information retrieval techniques implemented from scratch without external NLP libraries.

Author

Poojasri@2026

poojasri.connect@gmail.com
