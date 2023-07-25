import streamlit as st
import requests
import pickle

#import movies model
movies = pickle.load(open('/app/movies.pkl','rb'))


#Header Display
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'Select Movie',
movies['title'].values
)

if st.button("Recommend"):
    pass

