from pathlib import Path

import joblib
import pandas as pd


# ============================================================
# PATH CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "models"

TFIDF_PATH = MODEL_DIR / "tfidf_vectorizer.pkl"
SIMILARITY_PATH = MODEL_DIR / "cosine_similarity.pkl"
BOOKS_PATH = MODEL_DIR / "books_data.pkl"


# ============================================================
# LOAD SAVED COMPONENTS
# ============================================================

tfidf = joblib.load(TFIDF_PATH)

cosine_sim = joblib.load(SIMILARITY_PATH)

books = pd.read_pickle(BOOKS_PATH)


# ============================================================
# CREATE TITLE INDEX
# ============================================================

indices = pd.Series(
    books.index,
    index=books["Title"]
).drop_duplicates()


# ============================================================
# RECOMMEND BOOKS
# ============================================================

def recommend_books(title, num_recommendations=5):

    if title not in indices:
        return pd.DataFrame()

    book_index = indices[title]

    similarity_scores = list(
        enumerate(cosine_sim[book_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Remove selected book
    similarity_scores = [
        item
        for item in similarity_scores
        if item[0] != book_index
    ]

    # Select top recommendations
    top_books = similarity_scores[
        :num_recommendations
    ]

    recommendations = []

    for index, score in top_books:

        recommendations.append({
            "Title": books.loc[index, "Title"],
            "Author": books.loc[index, "Author"],
            "Genre": books.loc[index, "Genre"],
            "Publisher": books.loc[index, "Publisher"],
            "Similarity": round(score, 4)
        })

    return pd.DataFrame(recommendations)