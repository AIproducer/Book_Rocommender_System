# 📚 Book Recommender System

A content-based book recommendation system built with Python and Machine Learning.  
The application recommends books similar to a selected title using book metadata such as author, genre, and publisher.

## 🚀 Live Demo

[Try the Book Recommender System](https://bookrocommendersystem-1.streamlit.app/)

## 📌 Project Overview

This project implements a content-based recommendation approach to find books that are similar to a user's selected book.

The system uses:

- TF-IDF Vectorization
- Cosine Similarity
- Content-Based Filtering
- Python
- Pandas
- Scikit-learn
- Streamlit

## 🔍 Dataset

The dataset contains **211 books** with information including:

- Title
- Author
- Genre
- Height
- Publisher

Missing author and publisher values were handled during preprocessing.

## ⚙️ Recommendation Pipeline

```text
Book Dataset
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Combined Book Features
     ↓
TF-IDF Vectorization
     ↓
Cosine Similarity
     ↓
Similar Book Ranking
     ↓
Top-N Recommendations




🧠 How It Works

Book metadata is combined into a single feature representation.

TF-IDF converts the textual features into numerical vectors, and cosine similarity measures how similar two books are.

When a user selects a book, the system finds the most similar books and displays their:

Title
Author
Genre
Publisher
Similarity Score
📊 Exploratory Data Analysis

The project includes analysis of:

Missing values
Duplicate titles
Genre distribution
Top authors
Top publishers
Book height statistics
Most common genres and authors
🖥️ Streamlit Application

The Streamlit application provides:

Book selection dropdown
Number-of-recommendations control
Selected-book information
Similar-book recommendations
Similarity scores
Clean interactive interface
📂 Project Structure
Book_Recommender_System/
│
├── data/
│   └── books.csv
│
├── models/
│   ├── books_data.pkl
│   ├── cosine_similarity.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebooks/
│   └── 01_book_recommender_eda.ipynb
│
├── src/
│   └── recommender.py
│
├── tests/
│
├── images/
│
├── reports/
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
🛠️ Technologies

Python • Pandas • NumPy • Scikit-learn • Streamlit • Joblib

👨‍💻 Developer

Muhammad Ishfaq

Data Science | Machine Learning | NLP | Python

🌐 Live Application

Open the live application


### 2. Save and push

Run:

```powershell
git add README.md
git commit -m "Improve project documentation"
git push
