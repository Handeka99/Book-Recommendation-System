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