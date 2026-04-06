from fastapi import FastAPI
from loader import load_documents
from preprocess import process_documents, preprocess
from vectorizer import (
    build_vocabulary,
    compute_all_tf,
    compute_idf,
    compute_tfidf
)

app = FastAPI()
documents = load_documents("documents")
processed_docs = process_documents(documents)

vocab = build_vocabulary(processed_docs)
tf_vectors = compute_all_tf(processed_docs, vocab)
idf = compute_idf(processed_docs, vocab)
tfidf_vectors = compute_tfidf(tf_vectors, vocab, idf)

from fastapi.responses import FileResponse, RedirectResponse

@app.get("/")
def home():
    return FileResponse("static/index.html")

def compute_query_tfidf(query):
    tokens = preprocess(query)
    total_words = len(tokens)

    query_vector = []

    for word in vocab:
        count = tokens.count(word)
        tf = count / total_words if total_words > 0 else 0
        tfidf = tf * idf.get(word, 0)
        query_vector.append(tfidf)

    return query_vector



def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))

    norm1 = sum(a * a for a in vec1) ** 0.5
    norm2 = sum(b * b for b in vec2) ** 0.5

    if norm1 == 0 or norm2 == 0:
        return 0

    return dot_product / (norm1 * norm2)



@app.get("/search")
def search(q: str):
    query_vector = compute_query_tfidf(q)

    scores = []

    for doc_name, doc_vector in tfidf_vectors.items():
        score = cosine_similarity(query_vector, doc_vector)
        scores.append((doc_name, score))

    
    scores.sort(key=lambda x: x[1], reverse=True)

    top_3 = scores[:3]

    results = []

    for doc_name, score in top_3:
        snippet = documents[doc_name][:200].replace("**", "").replace("\n", " ")

        results.append({
            "document": doc_name,
            "score": round(score, 4),
            "snippet": snippet
        })

    return {"results": results}