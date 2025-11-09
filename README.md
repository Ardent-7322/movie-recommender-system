# 🎬 Movie Recommender System (Content-Based)

<!-- <p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/69/Tmdb-new-logo.svg" height="120" />
</p> -->

This project is a **Content-Based Movie Recommendation System** that suggests movies based on their **content attributes**.  
Using the **TMDB 5000 Movie Dataset**, the system analyzes metadata such as **genres, cast, crew, and keywords**, and recommends movies similar to the one selected.

---


<!-- <p align="center">
  <img src="assets/ui-home.png" width="600" alt="Home UI preview"/>
</p>

<p align="center">
  <img src="assets/ui-recommendation.png" width="600" alt="Recommendation Output Preview"/>
</p>

--- -->

##  Features

-  Content-based movie similarity engine
-  Uses **Vectorization** + **Cosine Similarity**
-  Searches and recommends similar movies instantly
-  Interactive **Streamlit-based UI**
-  Clean and easy-to-understand logic

---

##  Dataset

Dataset Used: **TMDB 5000 Movies & Credits**

| File | Description |
|------|-------------|
| `tmdb_5000_movies.csv` | Movie details such as title, genres, keywords, overview |
| `tmdb_5000_credits.csv` | Information about cast and crew |

 Dataset Source: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## System Architecture

<!-- <p align="center">
  <img src="assets/architecture-diagram.png" width="650" alt="System Architecture Diagram (placeholder)">
</p> -->

---

##  How It Works

### 1) Data Preprocessing
- Extract genres, keywords, cast, crew from structured fields
- Convert JSON-like structures to clean lists

### 2) Feature Engineering
A new feature column **`tags`** is created by combining:




### 3) Text Vectorization
`CountVectorizer` converts text into a feature matrix.

### 4) Similarity Measurement
Similarity between movies is calculated using **Cosine Similarity**.

### 5) Recommendation
Top **N most similar movies** are returned for any selected movie.

---

##  Tech Stack

| Layer | Tools Used |
|------|------------|
| **Language** | Python |
| **Libraries** | Pandas, NumPy, Scikit-learn |
| **Vectorization** | CountVectorizer |
| **Similarity** | Cosine Similarity |
| **UI Framework** | Streamlit (Frontend) |

---

##  Installation & Setup

```bash
# Clone this repository
git clone https://github.com/Ardent-7322/movie-recommender-system

# Navigate to the project folder
cd movie-recommender-system

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py


Input Movie: Avatar (2009)

Top Recommendations:
1. John Carter
2. Guardians of the Galaxy
3. Star Trek Beyond
4. The Adventures of Tintin
5. Jupiter Ascending
