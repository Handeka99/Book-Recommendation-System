import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#for content based filtering
from sklearn.metrics.pairwise import linear_kernel

#for collaborative filtering
import os
import math
import random
from surprise import accuracy, Reader, Dataset, NormalPredictor, KNNBasic, SVD, SVDpp

# Load datasets
Ratings = pd.read_csv('Ratings.csv')
Books = pd.read_csv('DataGabungan.csv')

# Updating column names in ratings dataset
Ratings.rename(columns={"User-ID": "user_id", "Book-Rating": "rating"}, inplace=True)
Ratings = Ratings[Ratings['rating'] != 0]

counters = Ratings.groupby(['user_id', 'ISBN']).size().reset_index(name='rating_count')

# Filter users who have rated more than 30 books and books that have more than 40 ratings
user_filter = counters.groupby('user_id').size() >= 30
book_filter = counters.groupby('ISBN').size() >= 40

# Apply the filters to the original dataset
Ratings = Ratings[Ratings['user_id'].isin(user_filter[user_filter].index) & Ratings['ISBN'].isin(book_filter[book_filter].index)]

Books.drop(['Unnamed: 0', 'user_id', 'rating'], axis=1, inplace=True)

# To have reproducible experiments
my_seed = 0
random.seed(my_seed)
np.random.seed(my_seed)

# Load the full dataset
reader = Reader(rating_scale=(1, 10))
data = Dataset.load_from_df(Ratings, reader)

# Shuffle the ratings for unbiased result
all_ratings = data.raw_ratings
random.shuffle(all_ratings)

# Split data into train and test data with the ratio 70:30
threshold = int(0.7 * len(all_ratings))
train_ratings = all_ratings[:threshold]
test_ratings = all_ratings[threshold:]

def book_read(user_id):
    '''Take user_id and return list of book that user has read'''
    books_list = list(Books['ISBN'])
    book_read_list = list(Ratings['ISBN'][Ratings['user_id'] == user_id])
    return books_list, book_read_list
# Initialize algorithms
npred = NormalPredictor()
knn = KNNBasic(sim_options={"name": "cosine", "user_based": True})
svd = SVD(random_state=0)
svdpp = SVDpp(random_state=0)

# Train models
def train_models():
    data.raw_ratings = train_ratings
    npred.fit(data.build_full_trainset())
    knn.fit(data.build_full_trainset())
    svd.fit(data.build_full_trainset())
    svdpp.fit(data.build_full_trainset())

train_models()

def get_recommendation(model, user_id, n=5):
    '''Give n recommendation to user_id using the specified model'''
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
        return "Please reduce your recommendation request"

def get_model(name):
    if name == 'Normal Predictor':
        return npred
    elif name == 'KNN':
        return knn
    elif name == 'SVD':
        return svd
    elif name == 'SVD++':
        return svdpp
    else:
        return None