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
from functions import prepare_data, train_models, get_model, get_recommendation

st.title("Book Recommendation System")

user_id = st.text_input("Enter User ID:")
method = st.selectbox("Select Method:", ["Normal Predictor", "KNN", "SVD", "SVD++"])
n = st.number_input("Number of Recommendations:", min_value=1, max_value=20, value=5)

# Load and prepare data
data, train_ratings, test_ratings, Books, Ratings = prepare_data()

if st.button("Train Models"):
    npred, knn, svd, svdpp = train_models(data, train_ratings)
    st.session_state['models'] = {'Normal Predictor': npred, 'KNN': knn, 'SVD': svd, 'SVD++': svdpp}
    st.success("Models trained successfully!")

if st.button("Recommend"):
    if 'models' in st.session_state:
        models = st.session_state['models']
        model = get_model(method, models['Normal Predictor'], models['KNN'], models['SVD'], models['SVD++'])
        if model:
            recommendations = get_recommendation(model, user_id, Books, Ratings, n)
            if isinstance(recommendations, pd.DataFrame):
                st.write(recommendations)
            else:
                st.write(recommendations)
        else:
            st.write("Invalid Method Selected")
    else:
        st.error("Please train the models first.")

