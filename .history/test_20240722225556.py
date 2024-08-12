import streamlit as st
import pandas as pd
import numpy as np
import random
from surprise import Reader, Dataset
from joblib import load


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

# Load data
Ratings = pd.read_csv('Ratings.csv')
Books = pd.read_csv('DataGabungan.csv')
Ratings.rename(columns={"User-ID": "user_id", "Book-Rating": "rating"}, inplace=True)
Ratings = Ratings[Ratings['rating'] != 0]

# Filter data
counters = Ratings.groupby('ISBN')['user_id'].nunique().reset_index(name='user_count')
book_filter = counters[counters['user_count'] >= 40]['ISBN']
user_filter = Ratings.groupby('user_id').size() >= 30
Ratings = Ratings[Ratings['user_id'].isin(user_filter[user_filter].index) & Ratings['ISBN'].isin(book_filter)]
Books.drop(['Unnamed: 0', 'user_id', 'rating'], axis=1, inplace=True)

# Load the full dataset
reader = Reader(rating_scale=(1, 10))
data = Dataset.load_from_df(Ratings, reader)

def book_read(user_id):
    '''Take user_id and return list of book that user has read'''
    books_list = list(Books['ISBN'])
    book_read_list = list(Ratings['ISBN'][Ratings['user_id'] == user_id])
    return books_list, book_read_list

# Load models
npred = load('npred_model.joblib')
knn = load('knn_model.joblib')
svd = load('svd_model.joblib')
svdpp = load('svdpp_model.joblib')

st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ['Top 20 Books', 'Recommend a Book'])

def get_recommendation(model, user_id, n=5):
    '''Give n recommendation to user_id using the selected model'''
    all_books, user_books = book_read(user_id)
    next_books = [book for book in all_books if book not in user_books]

    if n <= len(next_books):
        ratings = []
        for book in next_books:
            est = model.predict(user_id, book).est
            ratings.append((book, est))
        ratings = sorted(ratings, key=lambda x: x[1], reverse=True)
        book_ids = [id for id, rate in ratings[:n]]
        return Books[Books.ISBN.isin(book_ids)][['ISBN', 'title', 'author', 'average_rating', 'count_ratings']]
    else:
        st.write('Please reduce your recommendation request')
        return

# Streamlit UI
st.title('Book Recommendation System')
user_id = st.number_input('Enter User ID', min_value=0, step=1)
method = st.selectbox('Select Recommendation Method', ('NormalPredictor', 'KNNBasic', 'SVD', 'SVD++'))
n_recommendations = st.slider('Number of Recommendations', min_value=1, max_value=10, value=5)

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

if st.button('Get Recommendations'):
    if method == 'NormalPredictor':
        recommendations = get_recommendation(npred, user_id, n_recommendations)
    elif method == 'KNN':
        recommendations = get_recommendation(knn, user_id, n_recommendations)
    elif method == 'SVD':
        recommendations = get_recommendation(svd, user_id, n_recommendations)
    elif method == 'SVD++':
        recommendations = get_recommendation(svdpp, user_id, n_recommendations)
    
    if recommendations is not None:
        st.write(recommendations)
