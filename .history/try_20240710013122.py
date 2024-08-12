# import streamlit as st
# import numpy as np
# import pandas as pd
# import requests
# from streamlit_lottie import st_lottie



# st.sidebar.success("Best Ways To Find Your Books")

# st.markdown(f'<span style="color:black; font-size:28px; display: block; margin: 22px;"><b>Book Recommender System Using Machine Learning</b></span>', unsafe_allow_html=True)


# model = pd.read_pickle(open('D:/books/artifacts/model.pkl','rb'))
# book_names = pd.read_pickle(open('D:/books/artifacts/book_names.pkl','rb'))
# final_rating = pd.read_pickle(open('D:/books/artifacts/final_rating.pkl','rb'))
# book_pivot = pd.read_pickle(open('D:/books/artifacts/book_pivot.pkl','rb'))


# def fetch_poster(suggestion):
#     book_name = []
#     ids_index = []
#     poster_url = []

#     for book_id in suggestion:
#         book_name.append(book_pivot.index[book_id])

#     for name in book_name[0]: 
#         ids = np.where(final_rating['title'] == name)[0][0]
#         ids_index.append(ids)

#     for idx in ids_index:
#         url = final_rating.iloc[idx]['image_url']
#         poster_url.append(url)

#     return poster_url



# def recommend_book(book_name):
#     books_list = []
#     book_id = np.where(book_pivot.index == book_name)[0][0]
#     distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6 )

#     poster_url = fetch_poster(suggestion)
    
#     for i in range(len(suggestion)):
#             books = book_pivot.index[suggestion[i]]
#             for j in books:
#                 books_list.append(j)
#     return books_list , poster_url       
    
# selected_books = st.selectbox("", book_names)

# st.markdown("""
# <style>
# .stButton > button {
#     display: block;
#     margin: 0 auto;
#     background-color: green;
#     color: white;
# }
            
# .stButton > button:hover {
#     color: black;
#     border: 2px solid green;
#     box-shadow: 0 8px 20px 0 rgba(0,0,0,0.2);
    
# }
# </style>
# """, unsafe_allow_html=True)

# card_css = """
# <style>
# .text-black {
#     color: black;
# }

# .card {
#     box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
#     transition: 0.3s;
#     width: 100%;
#     background-color: white;
#     border-radius: 5px;
# }

# .card:hover {
#     box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
# }

# img {
#     height: 300px;
#     border-radius: 5px 5px 0 0;
# }

# .card-content {
#     padding: 10px;
# }
# </style>
# """

# def create_card_item(book_name, poster_url):
#     st.markdown(card_css, unsafe_allow_html=True)
#     col1, col2 = st.columns([1, 3])
#     with col1:
#         st.image(poster_url, use_column_width=True)
#     with col2:
#         st.markdown("""
#         <div class="card">
#             <div class="card-content">
#                 <h3 class='text-black'>{book_name}</h3>
#                 <p class='text-black'>Author:</p>
#                 <p class='text-black'>Year Book: </p>
#                 <p class='text-black'>Rating:</p>
#                 <p class='text-black'>ISBN: </p>
#                 <p class='text-black'>Publisher: </p>
#             </div>
#         </div>
#         """.format(book_name=book_name), unsafe_allow_html=True)

# if st.button('Find Books'):
#     recommended_books, poster_urls= recommend_book(selected_books)

#     for book, url in zip(recommended_books[1:], poster_urls[1:]):
#         create_card_item(book, url)




# footer_css = """
#     <style>
#         footer {
#         position: relative;
#         left: 0;
#         bottom: -20px;
#         width: 100%;
#         background-color: #333;
#         color: #fff;
#         text-align: center;
#         padding: 10px;
#         font-size: 12px;
#         }
#     </style>
# """

# footer_html = """
#     <footer>
#         <p>&copy; 2024 Book Recommender System. All rights reserved.</p>
#         <p>Developed by Find The Books</p>
#     </footer>
# """

# st.markdown(footer_css, unsafe_allow_html=True)
# st.markdown(footer_html, unsafe_allow_html=True)


