import streamlit as st

from src.recommender import recommend_books, books


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Book Recommender System",
    page_icon="📚",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .book-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #ddd;
        margin-bottom: 15px;
    }

    .book-title {
        font-size: 21px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📚 Book Recommender System</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Discover books similar to your favorite titles using
    Machine Learning
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("⚙️ Settings")

num_recommendations = st.sidebar.slider(
    "Number of recommendations",
    min_value=3,
    max_value=10,
    value=5
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    ### 🤖 How it works

    This application uses:

    • TF-IDF Vectorization  
    • Cosine Similarity  
    • Content-Based Filtering  

    Recommendations are generated using
    book metadata such as genre, author,
    and publisher.
    """
)


# ============================================================
# BOOK LIST
# ============================================================

book_titles = sorted(
    books["Title"]
    .dropna()
    .unique()
    .tolist()
)


# ============================================================
# SEARCH / SELECT BOOK
# ============================================================

st.subheader("🔍 Find a Book")

selected_book = st.selectbox(
    "Select a book:",
    book_titles
)


# ============================================================
# SELECTED BOOK INFORMATION
# ============================================================

selected_info = books[
    books["Title"] == selected_book
]

if not selected_info.empty:

    book = selected_info.iloc[0]

    st.markdown("### 📖 Selected Book")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Title**")
        st.write(book["Title"])

    with col2:
        st.write("**Author**")
        st.write(book["Author"])

    with col3:
        st.write("**Genre**")
        st.write(book["Genre"])


# ============================================================
# RECOMMEND BUTTON
# ============================================================

st.markdown("")

recommend_button = st.button(
    "🎯 Get Recommendations",
    type="primary",
    use_container_width=True
)


# ============================================================
# RECOMMENDATIONS
# ============================================================

if recommend_button:

    recommendations = recommend_books(
        selected_book,
        num_recommendations
    )

    if recommendations.empty:

        st.error(
            "No recommendations found."
        )

    else:

        st.markdown("---")

        st.subheader(
            f"📚 Books Similar to '{selected_book}'"
        )

        for rank, (_, row) in enumerate(
            recommendations.iterrows(),
            start=1
        ):

            st.markdown(
                f"""
                <div class="book-card">

                <div class="book-title">
                {rank}. {row["Title"]}
                </div>

                <b>✍️ Author:</b>
                {row["Author"]}<br>

                <b>🏷️ Genre:</b>
                {row["Genre"]}<br>

                <b>🏢 Publisher:</b>
                {row["Publisher"]}<br>

                <b>⭐ Similarity Score:</b>
                {row["Similarity"]:.4f}

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#777;">

    📚 <b>Book Recommender System</b><br>
    Developed By Muhammad ishfaq

    Built with Python • Pandas • Scikit-learn • Streamlit

    </div>
    """,
    unsafe_allow_html=True
)