import streamlit as st
import pickle

# Load the function from file
with open('book_read_function.pkl', 'rb') as f:
    book_read = pickle.load(f)

# Streamlit App
st.title("Book Recommendation App")

user_id = st.text_input("Enter User ID")

if st.button("Book From User ID"):
    if user_id:
        try:
            user_id = int(user_id)
            books_list, book_read_list = book_read(user_id)
            st.write("Books List:", books_list)
            st.write("Books Read by User:", book_read_list)
        except ValueError:
            st.error("Invalid User ID. Please enter a numeric User ID.")
    else:
        st.error("Please enter a User ID.")
