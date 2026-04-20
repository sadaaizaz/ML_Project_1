import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('D:\\coding\\domain\\project1\\archive\\tmdb_5000_movies.csv')
df = df[['title', 'overview', 'genres']]
df.fillna('', inplace=True)

df['combined'] = df['overview'] + ' ' + df['genres']
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(df['combined']).toarray()

similarity = cosine_similarity(vectors)

def recommend(movie):
    movie = movie.lower()
    if movie not in df['title'].str.lower().values:
        return "Movie not found!"

    idx = df[df['title'].str.lower() == movie].index[0]
    distances = similarity[idx]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    for i in movies_list:
        st.markdown("🍿 " + df.iloc[i[0]].title)

recommend("Avatar")