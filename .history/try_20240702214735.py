import streamlit as st
import numpy as np
import pandas as pd
import requests
from streamlit_lottie import st_lottie

# st.markdown("""
# <link
#   rel="stylesheet"
#   href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
#   integrity="sha512-iBBXm8fW90+nuLcSKlbmrPcLa0OT92xO1BIsZ+ywDWZCvqsWgccV3gFoRBv0z+8dLJgyAHIhR35VZc2oM/gI1w=="
#   crossorigin="anonymous"
#   referrerpolicy="no-referrer"
# />
# """, unsafe_allow_html=True)

page_bg_img= """
<style>
[data-testid="stAppViewContainer"]{
    # background-color: #fefbd8;
   
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center center;
  background-repeat: repeat;
  background-image: url("data:image/svg+xml;utf8,%3Csvg width=%222000%22 height=%221400%22 xmlns=%22http:%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cstyle%3E.shadow_right{-webkit-filter:drop-shadow(-5px -5px 15px %231d03ff);filter:drop-shadow(-5px -5px 15px %231d03ff)}.shadow_left{-webkit-filter:drop-shadow(5px 5px 15px %231d03ff);filter:drop-shadow(5px 5px 15px %231d03ff)}%3C%2Fstyle%3E%3Cdefs%3E%3ClinearGradient id=%22gradient__0%22 x1=%220%22 y1=%220%22 x2=%220%22 y2=%221%22%3E%3Cstop stop-color=%22%231d03ff%22 offset=%220%25%22%2F%3E%3Cstop stop-color=%22%237f86f3%22 offset=%2216.7%25%22%2F%3E%3Cstop stop-color=%22%23efedff%22 offset=%2233.3%25%22%2F%3E%3Cstop stop-color=%22%23fff%22 offset=%2250%25%22%2F%3E%3Cstop stop-color=%22%23efedff%22 offset=%2266.7%25%22%2F%3E%3Cstop stop-color=%22%237f86f3%22 offset=%2283.3%25%22%2F%3E%3Cstop stop-color=%22%231d03ff%22 offset=%22100%25%22%2F%3E%3C%2FlinearGradient%3E%3Cfilter id=%22grain%22 x=%22-1000%22 y=%22-700%22 width=%224000%22 height=%222800%22 filterUnits=%22userSpaceOnUse%22%3E&gt;%3CfeFlood flood-color=%22%23fff%22 result=%22neutral-gray%22%2F%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%222.5%22 numOctaves=%22100%22 stitchTiles=%22stitch%22 result=%22noise%22%2F%3E%3CfeColorMatrix in=%22noise%22 type=%22saturate%22 values=%220%22 result=%22destaturatedNoise%22%2F%3E%3CfeComponentTransfer in=%22desaturatedNoise%22 result=%22theNoise%22%3E%3CfeFuncA type=%22table%22 tableValues=%220 0 0.4 0%22%2F%3E%3C%2FfeComponentTransfer%3E%3CfeBlend in=%22SourceGraphic%22 in2=%22theNoise%22 mode=%22soft-light%22 result=%22noisy-image%22%2F%3E%3C%2Ffilter%3E%3C%2Fdefs%3E%3Cg filter=%22url(%23grain)%22%3E%3Cpath fill=%22%231d03ff%22 d=%22M0 0h2000v1400H0z%22%2F%3E%3Cpath id=%22rect__4%22 fill=%22url(%23gradient__0)%22 d=%22M888.889 311.111h222.222v777.778H888.889z%22%2F%3E%3Cpath class=%22shadow_left%22 id=%22rect__5%22 fill=%22url(%23gradient__0)%22 d=%22M1111.111 233.333h222.222v933.333h-222.222z%22%2F%3E%3Cpath class=%22shadow_left%22 id=%22rect__6%22 fill=%22url(%23gradient__0)%22 d=%22M1333.333 155.556h222.222v1088.889h-222.222z%22%2F%3E%3Cpath class=%22shadow_left%22 id=%22rect__7%22 fill=%22url(%23gradient__0)%22 d=%22M1555.556 77.778h222.222v1244.444h-222.222z%22%2F%3E%3Cpath class=%22shadow_left%22 id=%22rect__8%22 fill=%22url(%23gradient__0)%22 d=%22M1777.778 0H2000v1400h-222.222z%22%2F%3E%3Cpath class=%22shadow_right%22 id=%22rect__3%22 fill=%22url(%23gradient__0)%22 d=%22M666.667 233.333h222.222v933.333H666.667z%22%2F%3E%3Cpath class=%22shadow_right%22 id=%22rect__2%22 fill=%22url(%23gradient__0)%22 d=%22M444.444 155.556h222.222v1088.889H444.444z%22%2F%3E%3Cpath class=%22shadow_right%22 id=%22rect__1%22 fill=%22url(%23gradient__0)%22 d=%22M222.222 77.778h222.222v1244.444H222.222z%22%2F%3E%3Cpath class=%22shadow_right%22 id=%22rect__0%22 fill=%22url(%23gradient__0)%22 d=%22M0 0h222.222v1400H0z%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E");

}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.success("Best Ways To Find Your Books")

st.markdown(f'<span style="color:black; font-size:28px; display: block; margin: 22px;"><b>Book Recommender System Using Machine Learning</b></span>', unsafe_allow_html=True)


model = pd.read_pickle(open('D:/books/artifacts/model.pkl','rb'))
book_names = pd.read_pickle(open('D:/books/artifacts/book_names.pkl','rb'))
final_rating = pd.read_pickle(open('D:/books/artifacts/final_rating.pkl','rb'))
book_pivot = pd.read_pickle(open('D:/books/artifacts/book_pivot.pkl','rb'))


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



def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6 )

    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
            books = book_pivot.index[suggestion[i]]
            for j in books:
                books_list.append(j)
    return books_list , poster_url       
    
selected_books = st.selectbox("", book_names)

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

card_css = """
<style>
.text-black {
    color: black;
}

.card {
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
    width: 100%;
    background-color: white;
    border-radius: 5px;
}

.card:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

img {
    height: 300px;
    border-radius: 5px 5px 0 0;
}

.card-content {
    padding: 10px;
}
</style>
"""

def create_card_item(book_name, poster_url):
    st.markdown(card_css, unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(poster_url, use_column_width=True)
    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-content">
                <h3 class='text-black'>{book_name}</h3>
                <p class='text-black'>Author:</p>
                <p class='text-black'>Year Book: </p>
                <p class='text-black'>Rating:</p>
                <p class='text-black'>ISBN: </p>
                <p class='text-black'>Publisher: </p>
            </div>
        </div>
        """.format(book_name=book_name), unsafe_allow_html=True)

if st.button('Find Books'):
    recommended_books, poster_urls= recommend_book(selected_books)

    for book, url in zip(recommended_books[1:], poster_urls[1:]):
        create_card_item(book, url)

#gallery


#footer

footer_css = """
    <style>
        footer {
        position: relative;
        left: 0;
        bottom: -20px;
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


# st.markdown("""
# <style>
# footer {
#   background-color: var(--dark);
#   color: #fff;
#   text-align: center;
#   position: relative;
# }
# footer::before {
#   content: "";
#   position: absolute;
#   background-color: var(--green);
#   height: 4px;
#   top: 0;
#   left: 0;
#   width: 100%;
# }
# footer.site-brand {
#   margin-bottom: 1.5rem;
#   display: block;
#   font-size: 2rem!important;
# }
# .footer-item {
#   margin: 3rem 0;
# }
# .footer-item a {
#   font-size: 1.2rem;
#   color: #fff;
#   -webkit-transition: var(--trans);
#   -o-transition: var(--trans);
#   transition: var(--trans);
# }
# .footer-item a:hover {
#   color: var(--green);
# }
# .footer-item ul {
#   padding: 0;
# }
# .footer-item h2 {
#   margin-bottom: 1.4rem;
# }
# .social-links {
#   display: -webkit-box;
#   display: -ms-flexbox;
#   display: flex;
#   -webkit-box-pack: center;
#   -ms-flex-pack: center;
#   justify-content: center;
# }
# .social-links li {
#   margin: 0.5rem;
# }
# .footer-item:nth-child(3) li {
#   margin: 0.5rem 0;
# }
# .footer-item:nth-child(3) a {
#   display: inline-block;
#   font-size: 1rem;
#   opacity: 0.7;
# }
# .subscribe-form form {
#   -webkit-box-orient: vertical;
#   -webkit-box-direction: normal;
#   -ms-flex-direction: column;
#   flex-direction: column;
# }
# .subscribe-form form input {
#   width: 100%;
#   max-width: 300px;
# }
# .subscribe-form.form-control {
#   border-color: rgba(255, 255, 255, 0.3);
#   -webkit-transition: var(--trans);
#   -o-transition: var(--trans);
#   transition: var(--trans);
# }
# .subscribe-form.form-control:focus {
#   border-color: #fff;
# }
# .subscribe-form form input[type="email"]::-webkit-input-placeholder {
#   color: #fff;
#   opacity: 0.3;
# }
# .subscribe-form form input[type="email"]::-moz-placeholder {
#   color: #fff;
#   opacity: 0.3;
# }
# .subscribe-form form input[type="email"]:-ms-input-placeholder {
#   color: #fff;
#   opacity: 0.3;
# }
# .subscribe-form form input[type="email"]::-ms-input-placeholder {
#   color: #fff;
#   opacity: 0.3;
# }
# .subscribe-form form input[type="email"]::placeholder {
#   color: #fff;
#   opacity: 0.3;
# }

# header.header-sm {
#   min-height: 60vh;
# }
# </style>
# """, unsafe_allow_html=True)

# footer_html= """


#     <footer class="py-4">
#         <div class="container footer-row">
#             <div class="footer-item">
#             <a href="index.html" class="site-brand"> Mari<span>Liburan</span> </a>
#             <p class="text">
#                 Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet
#                 voluptates maiores nam vitae iusto. Placeat rem sint voluptas natus
#                 exercitationem autem quod neque, odit laudantium reiciendis ipsa
#                 suscipit veritatis voluptate.
#             </p>
#             </div>

#             <div class="footer-item">
#             <h2>Follow us on:</h2>
#             <ul class="social-links">
#                 <li>
#                 <a href="#">
#                     <i class="fab fa-facebook-f"></i>
#                 </a>
#                 </li>
#                 <li>
#                 <a href="#">
#                     <i class="fab fa-instagram"></i>
#                 </a>
#                 </li>
#                 <li>
#                 <a href="#">
#                     <i class="fab fa-twitter"></i>
#                 </a>
#                 </li>
#                 <li>
#                 <a href="#">
#                     <i class="fab fa-pinterest"></i>
#                 </a>
#                 </li>
#                 <li>
#                 <a href="#">
#                     <i class="fab fa-google-plus"></i>
#                 </a>
#                 </li>
#             </ul>
#             </div>

#             <div class="footer-item">
#             <h2>Popular Places:</h2>
#             <ul>
#                 <li><a href="#">Indonesia</a></li>
#                 <li><a href="#">Japan</a></li>
#                 <li><a href="#">Malaysia</a></li>
#                 <li><a href="#">Korea</a></li>
#                 <li><a href="#">Maldives</a></li>
#             </ul>
#             </div>

#             <div class="subscribe-form footer-item">
#             <h2>Subscribe for Newsletter!</h2>
#             <form class="flex">
#                 <input
#                 type="email"
#                 placeholder="Enter Email"
#                 class="form-control"
#                 />
#                 <input type="submit" class="btn" value="Subscribe" />
#             </form>
#             </div>
#         </div>
#         </footer>
#     """



