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



# import streamlit as st
# import numpy as np
# import pandas as pd

# page_bg_img= """
# <style>
# [data-testid="stAppViewContainer"]{
#     # background-color: #fefbd8;
   
#   width: 100%;
#   height: 100%;
#   background-size: cover;
#   background-position: center center;
#   background-repeat: repeat;
#   background-image: url("data:image/svg+xml;utf8,%3Csvg width=%222000%22 height=%221400%22 xmlns=%22http:%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cstyle%3E.shadow_right{-webkit-filter:drop-shadow(-5px -5px 15px %231d03ff);filter:drop-shadow(-5px -5px 15px %231d03ff)}.shadow_left{-webkit-filter:drop-shadow(5px 5px 15px %231d03ff);filter:drop-shadow(5px 5px 15px %231d03ff)}%3C%2Fstyle%3E%3Cdefs%3E%3ClinearGradient id=%22gradient__0%22 x1=%220%22 y1=%220%22 x2=%220%22 y2=%221%22%3E%3Cstop stop-color=%22%231d03ff%22 offset=%220%25%22%2F%3E%3Cstop stop-color=%22%237f86f3%22 offset=%2216.7%25%22%2F%3E%3Cstop stop-color=%22%23efedff%22 offset=%2233.3%25%22%2F%3E%3Cstop stop-color=%22%23fff%22 offset=%2250%25%22%2F%3E%3Cstop stop-color=%22%23efedff%22 offset=%2266.7%25%22%2F%3E%3Cstop stop-color=%22%237f86f3%22 offset=%2283.3%25%22%2F%3E%3Cstop stop-color=%22%231d03ff%22 offset=%22100%25%22%2F%3E%3C%2FlinearGradient%3E%3Cfilter id=%22grain%22 x=%22-1000%22 y=%22-700%22 width=%224000%22 height=%222800%22 filterUnits=%22userSpaceOnUse%22%3E&gt;%3CfeFlood flood-color=%22%23fff%22 result=%22neutral-gray%22%2F%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%222.5%22 numOctaves=%22100%22 stitchTiles=%22stitch%22 result=%22noise%22%2F%3E%3CfeColorMatrix in=%22noise%22 type=%22saturate%22 values=%220%22 result=%22destaturatedNoise%22%2F%3E%3CfeComponentTransfer in=%22desaturatedNoise%22 result=%22theNoise%22%3E%3CfeFuncA type=%22table%22 tableValues=%220 0 0.4 0%22%2F%3E%3C%2FfeComponentTransfer%3E%3CfeBlend in=%22SourceGraphic%22 in2=%22theNoise%22 mode=%22soft-light%22 result=%22noisy-image%22%2F%3E%3C%2Ffilter%3E%3C%2Fdefs%3E%3Cg filter=%22url(%23grain)%22%3E%3Cpath fill=%22%231d03ff%22 d=%22M0 0h2000v1400H0z%22%2F%3E%3Cpath id=%22rect__4%22 fill=%22url(%23gradient__0)%22 d=%22M888.889 311.111h222.222v777.778H888.889z%22%2F%3E%3Cpath class=%22shadow_left%22 id=%22rect__5%22 fill=%22url(%23gradient__0)%22 d=%22M1111.111 233.333h222.222v933.333h-222.222z%22%2F%3E%3Cpath class=%22shadow_left%22 id=%22rect__6%22 fill=%22url(%23gradient__0)%22 d=%22M1333.333 155.556h222.222v1088.889h-222.222z%22%2F%3E%3Cpath class=%22shadow_left%22 id=%22rect__7%22 fill=%22url(%23gradient__0)%22 d=%22M1555.556 77.778h222.222v1244.444h-222.222z%22%2F%3E%3Cpath class=%22shadow_left%22 id=%22rect__8%22 fill=%22url(%23gradient__0)%22 d=%22M1777.778 0H2000v1400h-222.222z%22%2F%3E%3Cpath class=%22shadow_right%22 id=%22rect__3%22 fill=%22url(%23gradient__0)%22 d=%22M666.667 233.333h222.222v933.333H666.667z%22%2F%3E%3Cpath class=%22shadow_right%22 id=%22rect__2%22 fill=%22url(%23gradient__0)%22 d=%22M444.444 155.556h222.222v1088.889H444.444z%22%2F%3E%3Cpath class=%22shadow_right%22 id=%22rect__1%22 fill=%22url(%23gradient__0)%22 d=%22M222.222 77.778h222.222v1244.444H222.222z%22%2F%3E%3Cpath class=%22shadow_right%22 id=%22rect__0%22 fill=%22url(%23gradient__0)%22 d=%22M0 0h222.222v1400H0z%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E");

# }
# </style>
# """
# st.markdown(page_bg_img, unsafe_allow_html=True)


# # Load the models and data
# model = pd.read_pickle('D:/books/artifacts/model.pkl')
# book_names = pd.read_pickle('D:/books/artifacts/book_names.pkl')
# final_rating = pd.read_pickle('D:/books/artifacts/final_rating.pkl')
# book_pivot = pd.read_pickle('D:/books/artifacts/book_pivot.pkl')

# # Function to fetch book poster URLs
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

# # Function to recommend books based on a selected book
# def recommend_book(book_name):
#     books_list = []
#     book_id = np.where(book_pivot.index == book_name)[0][0]
#     distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)

#     poster_url = fetch_poster(suggestion)
    
#     for i in range(len(suggestion)):
#         books = book_pivot.index[suggestion[i]]
#         for j in books:
#             books_list.append(j)
#     return books_list, poster_url       

# # Function to get top 20 books based on highest ratings
# def top_20_books():
#     if 'rating' in final_rating.columns:
#         top_books = final_rating.sort_values(by='rating', ascending=False).head(20)
#         return top_books
#     else:
#         st.error("Column 'rating' not found in the final_rating DataFrame.")
#         return pd.DataFrame()

# # Function to create card item for book display
# def create_card_item(book_name, poster_url):
#     card_css = """
#     <style>
#     .card-container {
#         padding: 10px;
#     }
#     .card {
#         box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
#         transition: 0.3s;
#         width: 100%;
#         background-color: white;
#         border-radius: 5px;
#         margin-bottom: 20px;
#         display: flex;
#         flex-direction: column;
#         align-items: center;
#     }
#     .card:hover {
#         box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
#     }
#     img {
#         height: 150px;
#         border-radius: 5px 5px 0 0;
#         object-fit: cover;
#     }
#     .card-content {
#         padding: 10px;
#         text-align: center;
#     }
#     .text-black {
#         color: black;
#     }
#     </style>
#     """
#     st.markdown(card_css, unsafe_allow_html=True)
#     card_html = f"""
#     <div class="card-container">
#         <div class="card">
#             <img src="{poster_url}" alt="{book_name}">
#             <div class="card-content">
#                 <h4 class='text-black'>{book_name}</h4>
#                 <p class='text-black'><b>Author:</b></p>
#                 <p class='text-black'><b>Year:</b> </p>
#                 <p class='text-black'><b>Rating:</b> </p>
#                 <p class='text-black'><b>ISBN:</b> </p>
#                 <p class='text-black'><b>Publisher:</b> </p>
#             </div>
#         </div>
#     </div>
#     """
#     st.markdown(card_html, unsafe_allow_html=True)

# # Streamlit UI elements
# st.markdown("<h1 style='text-align: center;'>Top 20 Recommended Books</h1>", unsafe_allow_html=True)

# # Display the top 20 books based on highest ratings
# top_books = top_20_books()

# for index, row in top_books.iterrows():
#     create_card_item(row['title'], row['image_url'])

# # Footer
# footer_css = """
# <style>
# footer {
#     position: relative;
#     left: 0;
#     bottom: -20px;
#     width: 100%;
#     background-color: #333;
#     color: #fff;
#     text-align: center;
#     padding: 10px;
#     font-size: 12px;
# }
# </style>
# """
# footer_html = """
# <footer>
#     <p>&copy; 2024 Book Recommender System. All rights reserved.</p>
#     <p>Developed by Find The Books</p>
# </footer>
# """
# st.markdown(footer_css, unsafe_allow_html=True)
# st.markdown(footer_html, unsafe_allow_html=True)






import streamlit as st
import numpy as np
import pandas as pd

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
    background-color: #fefbd8;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center center;
    background-repeat: repeat;
    background-image: url("data:image/svg+xml;utf8,%3Csvg width=%222000%22 height=%221400%22 xmlns=%22http:%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cstyle%3E.shadow_right{-webkit-filter:drop-shadow(-5px -5px 15px %231d03ff);filter:drop-shadow(-5px -5px 15px %231d03ff)}.shadow_left{-webkit-filter:drop-shadow(5px 5px 15px %231d03ff);filter:drop-shadow(5px 5px 15px %231d03ff)}%3C%2Fstyle%3E%3Cdefs%3E%3ClinearGradient id=%22gradient__0%22 x1=%220%22 y1=%220%22 x2=%220%22 y2=%221%22%3E%3Cstop stop-color=%22%231d03ff%22 offset=%220%25%22%2F%3E%3Cstop stop-color=%22%237f86f3%22 offset=%2216.7%25%22%2F%3E%3Cstop stop-color=%22%23efedff%22 offset=%2233.3%25%22%2F%3E%3Cstop stop-color=%22%23fff%22 offset=%2250%25%22%2F%3E%3Cstop stop-color=%22%23efedff%22 offset=%2266.7%25%22%2F%3E%3Cstop stop-color=%22%237f86f3%22 offset=%2283.3%25%22%2F%3E%3Cstop stop-color=%22%231d03ff%22 offset=%22100%25%22%2F%3E%3C%2FlinearGradient%3E%3Cfilter id=%22grain%22 x=%22-1000%22 y=%22-700%22 width=%224000%22 height=%222800%22 filterUnits=%22userSpaceOnUse%22%3E%3E%3CfeFlood flood-color=%22%23fff%22 result=%22neutral-gray%22%2F%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%222.5%22 numOctaves=%22100%22 stitchTiles=%22stitch%22 result=%22noise%22%2F%3E%3CfeColorMatrix in=%22noise%22 type=%22saturate%22 values=%220%22 result=%22destaturatedNoise%22%2F%3E%3CfeComponentTransfer in=%22desaturatedNoise%22 result=%22theNoise%22%3E%3CfeFuncA type=%22table%22 tableValues=%220 0 0.4 0%22%2F%3E%3C%2FfeComponentTransfer%3E%3CfeBlend in=%22SourceGraphic%22 in2=%22theNoise%22 mode=%22soft-light%22 result=%22noisy-image%22%2F%3E%3C%2Ffilter%3E%3C%2Fdefs%3E%3Cg filter=%22url(%23grain)%22%3E%3Cpath fill=%22%231d03ff%22 d=%22M0 0h2000v1400H0z%22%2F%3E%3Cpath id=%22rect__4%22 fill=%22url(%23gradient__0)%22 d=%22M888.889 311.111h222.222v777.778H888.889z%22%2F%3E%3Cpath class=%22shadow_left%22 id=%22rect__5%22 fill=%22url(%23gradient__0)%22 d=%22M1111.111 233.333h222.222v933.333h-222.222z%22%2F%3E%3Cpath class=%22shadow_left%22 id=%22rect__6%22 fill=%22url(%23gradient__0)%22 d=%22M1333.333 155.556h222.222v1088.889h-222.222z%22%2F%3E%3Cpath class=%22shadow_left%22 id=%22rect__7%22 fill=%22url(%23gradient__0)%22 d=%22M1555.556 77.778h222.222v1244.444h-222.222z%22%2F%3E%3Cpath class=%22shadow_left%22 id=%22rect__8%22 fill=%22url(%23gradient__0)%22 d=%22M1777.778 0H2000v1400h-222.222z%22%2F%3E%3Cpath class=%22shadow_right%22 id=%22rect__3%22 fill=%22url(%23gradient__0)%22 d=%22M666.667 233.333h222.222v933.333H666.667z%22%3E%3Cpath class=%22shadow_right%22 id=%22rect__2%22 fill=%22url(%23gradient__0)%22 d=%22M444.444 155.556h222.222v1088.889H444.444z%22%3E%3Cpath class=%22shadow_right%22 id=%22rect__1%22 fill=%22url(%23gradient__0)%22 d=%22M222.222 77.778h222.222v1244.444H222.222z%22%3E%3Cpath class=%22shadow_right%22 id=%22rect__0%22 fill=%22url(%23gradient__0)%22 d=%22M0 0h222.222v1400H0z%22%3E%3C%2Fg%3E%3C%2Fsvg%3E");
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
        top_books = final_rating.sort_values(by='rating', ascending=False).head(20)
        return top_books
    else:
        st.error("Column 'rating' not found in the final_rating DataFrame.")
        return pd.DataFrame()

# Function to create card item for book display
def create_card_item(book_name, poster_url):
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
                <p class='text-black'><b>Author:</b></p>
                <p class='text-black'><b>Year:</b> </p>
                <p class='text-black'><b>Rating:</b> </p>
                <p class='text-black'><b>ISBN:</b> </p>
                <p class='text-black'><b>Publisher:</b> </p>
            </div>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ['Home', 'Top 20 Books', 'Recommend a Book'])

# Main page
if options == 'Home':
    st.markdown("<h1 style='text-align: center;'>Welcome to the Book Recommender System</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Use the navigation bar to explore top books and get recommendations.</p>", unsafe_allow_html=True)
elif options == 'Top 20 Books':
    st.markdown("<h1 style='text-align: center;'>Top 20 Recommended Books</h1>", unsafe_allow_html=True)
    top_books = top_20_books()
    for index, row in top_books.iterrows():
        create_card_item(row['title'], row['image_url'])
elif options == 'Recommend a Book':
    st.markdown("<h1 style='text-align: center;'>Book Recommendation System</h1>", unsafe_allow_html=True)
    book_list = book_pivot.index.tolist()
    selected_book = st.selectbox("Select a book to get recommendations:", book_list)
    if st.button("Recommend"):
        recommended_books, poster_urls = recommend_book(selected_book)
        for book, poster in zip(recommended_books, poster_urls):
            create_card_item(book, poster)

# Footer
footer_css = """
<style>
footer {
    position: absolute;
    left: 0;
    bottom: 0;
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

