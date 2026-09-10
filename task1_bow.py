import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer


corpus = [
    "The product performance is amazing and fast",
    "The service was fast and performance was great",
    "Terrible customer service and bad performance"
]

# Create CountVectorizer
vectorizer = CountVectorizer(stop_words="english")

# Convert text into Bag of Words matrix
X = vectorizer.fit_transform(corpus)

# Get vocabulary
vocabulary = vectorizer.get_feature_names_out()

print("\nVocabulary:")
print(vocabulary)

# Convert matrix into Pandas DataFrame
bow_df = pd.DataFrame(
    X.toarray(),
    columns=vocabulary
)

print("\nBag of Words Matrix:")
print(bow_df)