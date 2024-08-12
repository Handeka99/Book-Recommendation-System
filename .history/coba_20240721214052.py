# import streamlit as st
# import pandas as pd
# from functions import get_model, get_recommendation

# st.title("Book Recommendation System")

# user_id = st.text_input("Enter User ID:")
# method = st.selectbox("Select Method:", ["Normal Predictor", "KNN", "SVD", "SVD++"])
# n = st.number_input("Number of Recommendations:", min_value=1, max_value=20, value=5)

# if st.button("Recommend"):
#     model = get_model(method)
#     if model:
#         recommendations = get_recommendation(model, user_id, n)
#         if isinstance(recommendations, pd.DataFrame):
#             st.write(recommendations)
#         else:
#             st.write(recommendations)
#     else:
#         st.write("Invalid Method Selected")


import streamlit as st
import pandas as pd
import numpy as np
import random
from surprise import NormalPredictor, KNNBasic, SVD, SVDpp, Dataset, Reader, accuracy

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

# Load datasets
Ratings = pd.read_csv('Ratings.csv')
Books = pd.read_csv('DataGabungan.csv')

# Preprocess datasets
Ratings.rename(columns={"User-ID": "user_id", "Book-Rating": "rating"}, inplace=True)
Ratings = Ratings[Ratings['rating'] != 0]

counters = Ratings.groupby(['user_id', 'ISBN']).size().reset_index(name='rating_count')

# Filter users and books
user_filter = counters.groupby('user_id').size() >= 30
book_filter = counters.groupby('ISBN').size() >= 40

Ratings = Ratings[Ratings['user_id'].isin(user_filter[user_filter].index) &
                  Ratings['ISBN'].isin(book_filter[book_filter].index)]

Books.drop(['Unnamed: 0', 'user_id', 'rating'], axis=1, inplace=True)

# For reproducibility
my_seed = 0
random.seed(my_seed)
np.random.seed(my_seed)

# Load the full dataset
reader = Reader(rating_scale=(1, 10))
data = Dataset.load_from_df(Ratings, reader)

# Shuffle the ratings
all_ratings = data.raw_ratings
random.shuffle(all_ratings)

# Split data into train and test
threshold = int(0.7 * len(all_ratings))
train_ratings = all_ratings[:threshold]
test_ratings = all_ratings[threshold:]

def book_read(user_id):
    books_list = list(Books['ISBN'])
    book_read_list = list(Ratings['ISBN'][Ratings['user_id'] == user_id])
    return books_list, book_read_list

# Define the models
def get_model(model_name):
    if model_name == "Normal Predictor":
        return NormalPredictor()
    elif model_name == "KNN":
        sim_options = {"name": "cosine", "user_based": True}
        return KNNBasic(sim_options=sim_options)
    elif model_name == "SVD":
        return SVD(random_state=0)
    elif model_name == "SVD++":
        return SVDpp(random_state=0)

# Define the recommendation function
def get_recommendations(model, user_id, n=5):
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
        return pd.DataFrame()
    
# Streamlit Interface
st.title('Book Recommendation System')

# Input user_id
user_id = st.text_input('Enter User ID:', '')

# Select method
method = st.selectbox('Select Recommendation Method:', ('Normal Predictor', 'KNN', 'SVD', 'SVD++'))

# Button to get recommendations
if st.button('Recommend'):
    if user_id.isdigit():
        user_id = int(user_id)  # Ensure user_id is an integer
        # Get the selected model
        model = get_model(method)

        # Prepare train data
        data.raw_ratings = train_ratings
        model.fit(data.build_full_trainset())

        # Get recommendations
        recommendations = get_recommendations(model, user_id)
        
        # Display recommendations
        if not recommendations.empty:
            st.write('Recommendations:')
            st.dataframe(recommendations)
        else:
            st.write('No recommendations available or user not found.')
    else:
        st.write('Please enter a valid numeric User ID.')