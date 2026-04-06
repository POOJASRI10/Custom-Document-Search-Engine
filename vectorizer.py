def build_vocabulary(processed_docs):
    vocab = set()

    for tokens in processed_docs.values():
        vocab.update(tokens)

    return list(vocab)


def compute_tf(tokens, vocab):
    tf_vector = []
    total_words = len(tokens)

    for word in vocab:
        count = tokens.count(word)
        tf = count / total_words
        tf_vector.append(tf)

    return tf_vector


def compute_all_tf(processed_docs, vocab):
    tf_vectors = {}

    for doc_name, tokens in processed_docs.items():
        tf_vectors[doc_name] = compute_tf(tokens, vocab)

    return tf_vectors

import math

def compute_idf(processed_docs, vocab):
    N = len(processed_docs)
    idf = {}

    for word in vocab:
        doc_count = 0

        for tokens in processed_docs.values():
            if word in tokens:
                doc_count += 1

        # avoid division by zero
        idf[word] = math.log((N + 1) / (doc_count + 1)) + 1

    return idf

def compute_tfidf(tf_vectors, vocab, idf):
    tfidf_vectors = {}

    for doc_name, tf_vector in tf_vectors.items():
        tfidf_vector = []

        for i, word in enumerate(vocab):
            tfidf_value = tf_vector[i] * idf[word]
            tfidf_vector.append(tfidf_value)

        tfidf_vectors[doc_name] = tfidf_vector

    return tfidf_vectors