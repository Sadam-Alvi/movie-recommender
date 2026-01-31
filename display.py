
import streamlit as st
<<<<<<< HEAD
import pickle
import pandas as pd

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

def recommend(title):
    movie_index = pd.Series(df.index, index=df["original_title"]).drop_duplicates()
    idx = movie_index[title]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    recommended = [df.iloc[i[0]]["original_title"] for i in scores[1:6]]

    return recommended





=======
from app import movie_recommend  
import pandas as pd

>>>>>>> 1dc13e4356e874dcb0abf2eec991141eaf81c405
st.markdown("<h1 style='color: darkblue;'>🎬 Movie Recommender</h1>", unsafe_allow_html=True)
df = pd.read_csv("tmdb_5000_movies.csv")
# Dropdown
selected_movie = st.selectbox("Select a Movie 🎬 ",df["original_title"].values)


# Button to recommend
if st.button("Recommend"):
<<<<<<< HEAD
    recommendations = recommend(selected_movie)
=======
    recommendations = movie_recommend(selected_movie)
>>>>>>> 1dc13e4356e874dcb0abf2eec991141eaf81c405
    st.write("Top 5 recommended movies:")
    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. {movie}")
