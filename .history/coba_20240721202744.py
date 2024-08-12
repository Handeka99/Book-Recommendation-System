import streamlit as st
import pandas as pd
from functions import get_model, get_recommendation

st.title("Book Recommendation System")

user_id = st.text_input("Enter User ID:")
method = st.selectbox("Select Method:", ["Normal Predictor", "KNN", "SVD", "SVD++"])
n = st.number_input("Number of Recommendations:", min_value=1, max_value=20, value=5)

if st.button("Recommend"):
    model = get_model(method)
    if model:
        recommendations = get_recommendation(model, user_id, n)
        if isinstance(recommendations, pd.DataFrame):
            st.write(recommendations)
        else:
            st.write(recommendations)
    else:
        st.write("Invalid Method Selected")
