import streamlit as st
import pickle

# Load data
movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movies_list = movies['title'].values

st.header("Movie Recommender System")

selectvalue = st.selectbox("Select a movie from dropdown", movies_list)

def recommend(movie_name):
    # Find index of selected movie
    index = movies[movies['title'].str.strip().str.lower() == movie_name.strip().lower()].index[0]
    
    # Get list of similar movies
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    
    recommended_movies = []
    for i in distances[1:6]:  # skip first because it's the same movie
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies

if st.button("Show Recommend"):
    movie_names = recommend(selectvalue)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(movie_names[0])
    with col2:
        st.text(movie_names[1])
    with col3:
        st.text(movie_names[2])
    with col4:
        st.text(movie_names[3])
    with col5:
        st.text(movie_names[4])
