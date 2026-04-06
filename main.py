from loader import load_documents
from preprocess import process_documents, preprocess
from vectorizer import build_vocabulary, compute_all_tf, compute_idf, compute_tfidf

def compute_query_tfidf(query, vocab, idf):
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


def search(query, tfidf_vectors, vocab, idf, documents):
    query_vector = compute_query_tfidf(query, vocab, idf)

    scores = []

    for doc_name, doc_vector in tfidf_vectors.items():
        score = cosine_similarity(query_vector, doc_vector)
        scores.append((doc_name, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    top_3 = scores[:3]

    results = []

    for doc_name, score in top_3:
        content = documents[doc_name][:200]  # snippet

        results.append({
            "document": doc_name,
            "score": round(score, 4),
            "snippet": content
        })

    return results

if __name__ == "__main__":

    documents = load_documents("documents")
    processed_docs = process_documents(documents)

    
    vocab = build_vocabulary(processed_docs)
    tf_vectors = compute_all_tf(processed_docs, vocab)
    idf = compute_idf(processed_docs, vocab)
    tfidf_vectors = compute_tfidf(tf_vectors, vocab, idf)

    print("System ready. Type your query.\n")

    
    while True:
        query = input("Enter search query (or 'exit'): ")

        if query.lower() == "exit":
            break

        results = search(query, tfidf_vectors, vocab, idf, documents)

        print("\nTop Results:\n")

        for r in results:
            print(f"Document: {r['document']}")
            print(f"Score: {r['score']}")
            print(f"Snippet: {r['snippet']}")
            print("-" * 50)

        print("\n")