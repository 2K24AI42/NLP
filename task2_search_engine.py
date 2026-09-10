import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Machine learning algorithms analyze structured data effectively",
    "Deep learning and neural networks excel at processing unstructured data",
    "Natural language processing helps computers understand human language",
    "Python is widely used for machine learning and data science"
]

query = ["machine learning algorithms for data"]

search_vectorizer = CountVectorizer(stop_words="english")

doc_vectors = search_vectorizer.fit_transform(documents)

query_vector = search_vectorizer.transform(query)

similarity_scores = cosine_similarity(
    query_vector,
    doc_vectors
)[0]

results = []

for i, score in enumerate(similarity_scores):
    results.append((i + 1, score, documents[i]))

results.sort(key=lambda x: x[1], reverse=True)

print("\nSearch Results:")
print("=" * 70)

for rank, (doc_number, score, document) in enumerate(results, start=1):
    print(f"Rank {rank}")
    print(f"Document {doc_number}")
    print(f"Cosine Similarity: {score:.4f}")
    print(f"Text: {document}")
    print("-" * 70)