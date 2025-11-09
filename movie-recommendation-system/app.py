import streamlit as st
import pandas as pd
import pickle
import time
import random
import requests

st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id, title=None):
    """
    Fetches a movie poster from TMDB using movie_id.
    Includes retry logic, fallback search by title, and caching.
    """
    base = "https://api.themoviedb.org/3"
    api = "8265bd1679663a7ea12ac168da84d2e8"

    for attempt in range(3):  # Retry up to 3 times
        try:

            response = requests.get(
                f"{base}/movie/{movie_id}?api_key={api}&language=en-US",
                timeout=5
            )
            response.raise_for_status()
            data = response.json()
            poster_path = data.get("poster_path")

            if not poster_path and title:
                search = requests.get(
                    f"{base}/search/movie?api_key={api}&query={title}",
                    timeout=5
                )
                search.raise_for_status()
                results = search.json().get("results")
                if results:
                    poster_path = results[0].get("poster_path")


            if poster_path:
                return f"https://image.tmdb.org/t/p/w500/{poster_path}"
            else:
                return "https://via.placeholder.com/500x750?text=No+Image"

        except requests.exceptions.RequestException as e:
            print(f"⚠️ Attempt {attempt+1}/3 failed for {title or movie_id}: {e}")
            time.sleep(random.uniform(0.4, 1.2))


    return "https://via.placeholder.com/500x750?text=Error"


@st.cache_data(show_spinner=False)
def recommend(movie, movies, similarity):
    """
    Recommend top 5 similar movies based on cosine similarity matrix.
    Cached for faster performance.
    """
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    names, posters = [], []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        names.append(title)
        posters.append(fetch_poster(movie_id, title))
        time.sleep(0.2)  # small delay to prevent rate limit
    return names, posters


@st.cache_data(show_spinner=False)
def load_data():
    movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open("similarity.pkl", "rb"))
    return movies, similarity

movies, similarity = load_data()

st.title("🎬 Movie Recommender System")

movie_list = movies["title"].values

selected_movie = st.selectbox(
    "🔍 Type or select a movie to get similar recommendations:",
    movie_list,
    placeholder="Search for a movie...",
)

if st.button(" Show Recommendation") and selected_movie:
    with st.spinner("Fetching recommendations..."):
        time.sleep(0.5)
        names, posters = recommend(selected_movie, movies, similarity)

    st.subheader(f"Movies similar to **{selected_movie}**:")
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.image(posters[i])
            st.text(names[i])






