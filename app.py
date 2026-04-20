import streamlit as st
from main import recommend

st.title("🎬 Movie Recommender")

movie_name = st.text_input("Enter a movie name")

if st.button("Recommend"):
    recommend(movie_name)