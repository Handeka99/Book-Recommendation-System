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