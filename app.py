import streamlit as st
import pandas as pd
import pickle

# Load the pickled model
similarity = pickle.load(open('notebook/similarity.pkl', 'rb'))

# load book list
book_list = pd.read_csv("notebook\data\clean_books.csv")


# Getting the top 10 recommendations
def recommmend(book):
    index = book_list[book_list['Title']==book].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse= True,key = lambda x: x[1])
    recommended_books = []
    for i in distances[1:6]:
        recommended_books.append(str(book.iloc[i[0]].Title))
        return recommended_books

st.title("Books Recommender System")

selected_book = st.selectbox(
    'Select a book',
    book_list
)


if st.button('Recommend'):
    recommendations = recommmend(selected_book)
    for i in recommendations:
        st.write(i)