import streamlit as st
import numpy as np
import pandas as pd

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
    background-color: #ECCEAE;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center center;
    background-repeat: repeat;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the models and data
model = pd.read_pickle('D:/books/artifacts/model.pkl')
book_names = pd.read_pickle('D:/books/artifacts/book_names.pkl')
final_rating = pd.read_pickle('D:/books/artifacts/final_rating.pkl')
book_pivot = pd.read_pickle('D:/books/artifacts/book_pivot.pkl')

# Function to fetch book poster URLs
def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]: 
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['image_url']
        poster_url.append(url)

    return poster_url

# Function to recommend books based on a selected book
def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)

    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            books_list.append(j)
    return books_list, poster_url       

# Function to get top 20 books based on highest ratings
def top_20_books():
    if 'rating' in final_rating.columns:
        top_books = final_rating.drop_duplicates(subset='title').sort_values(by='rating', ascending=False).head(20)
        return top_books
    else:
        st.error("Column 'rating' not found in the final_rating DataFrame.")
        return pd.DataFrame()

# Function to create card item for book display
def create_card_item(book_name, poster_url, author, year, rating):
    card_css = """
    <style>
    .card-container {
        padding: 10px;
    }
    .card {
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        width: 100%;
        background-color: white;
        border-radius: 5px;
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    img {
        height: 150px;
        border-radius: 5px 5px 0 0;
        object-fit: cover;
    }
    .card-content {
        padding: 10px;
        text-align: center;
    }
    .text-black {
        color: black;
    }
    </style>
    """
    st.markdown(card_css, unsafe_allow_html=True)
    card_html = f"""
    <div class="card-container">
        <div class="card">
            <img src="{poster_url}" alt="{book_name}">
            <div class="card-content">
                <h4 class='text-black'>{book_name}</h4>
                <p class='text-black'><b>Author:</b>{author}</p>
                <p class='text-black'><b>Year:</b> {year}</p>
                <p class='text-black'><b>Rating:</b> {rating}</p>
            </div>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ['Top 20 Books', 'Recommend a Book'])


st.markdown("""
<style>
.stButton > button {
    display: block;
    margin: 0 auto;
    background-color: green;
    color: white;
}
            
.stButton > button:hover {
    color: black;
    border: 2px solid green;
    box-shadow: 0 8px 20px 0 rgba(0,0,0,0.2);
    
}
</style>
""", unsafe_allow_html=True)

# Main page
if options == 'Top 20 Books':
    st.markdown("<h1 style='text-align: center; color:black;'>Top 20 Recommended Books</h1>", unsafe_allow_html=True)
    top_books = top_20_books()
    for index, row in top_books.iterrows():
        create_card_item(row['title'], row['image_url'], row['author'], row['year'], row['rating'])
elif options == 'Recommend a Book':
    st.markdown("<h1 style='text-align: center; color: black;'>Book Recommendation System</h1>", unsafe_allow_html=True)
    user_id = st.text_input("Enter User ID")
    book_list = book_pivot.index.tolist()
    selected_book = st.selectbox("Select a Book", book_list)
    if st.button("Recommend"):
        recommended_books, poster_urls = recommend_book(selected_book)
        for book, poster in zip(recommended_books, poster_urls):
            book_data = final_rating[final_rating['title'] == book].iloc[0]
            create_card_item(book, poster, book_data['author'], book_data['year'], book_data['rating'])


# Footer
footer_css = """
<style>
footer {
    position: relative;
    left: 0;
    bottom: -20px;
    width: 100%;
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 10px;
    font-size: 12px;
}
</style>
"""
footer_html = """
<footer>
    <p>&copy; 2024 Book Recommender System. All rights reserved.</p>
    <p>Developed by Find The Books</p>
</footer>
"""
st.markdown(footer_css, unsafe_allow_html=True)
st.markdown(footer_html, unsafe_allow_html=True)
