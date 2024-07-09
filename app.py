import pickle
import streamlit as st
import requests

# Function to fetch the poster and details of the movie
def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    overview = data['overview']
    title = data['title']
    return full_path, title, overview

# Function to recommend movies based on the given movie title
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_ids = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        poster_path, title, overview = fetch_movie_details(movie_id)
        recommended_movie_posters.append(poster_path)
        recommended_movie_names.append(title)
        recommended_movie_ids.append(movie_id)

    return recommended_movie_names, recommended_movie_posters, recommended_movie_ids

# Streamlit UI setup
st.set_page_config(page_title='Movie Recommender System', page_icon='🎬', layout='wide', initial_sidebar_state='auto')
st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
        color: #fff;
    }
    .movie-poster:hover {
        transform: scale(1.05);
        transition: transform 0.2s;
        z-index: 10;
    }
    .movie-title {
        cursor: pointer;
        color: #ff4b4b;
        text-align: center;
    }
    .spinner {
        border: 4px solid rgba(0,0,0,.1);
        width: 36px;
        height: 36px;
        border-radius: 50%;
        border-left-color: #09f;
        animation: spin 1s ease infinite;
        margin: auto;
    }
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page header
st.header('🎬 Movie Recommender System')

# Load the movie data and similarity matrix
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Initialize session state for selected movie
if 'selected_movie' not in st.session_state:
    st.session_state.selected_movie = None

# Create a selectbox for movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list,
    index=movie_list.tolist().index(st.session_state.selected_movie) if st.session_state.selected_movie else 0,
    key='movie_selectbox'
)

# Update session state when a new movie is selected from the dropdown
if selected_movie != st.session_state.selected_movie:
    st.session_state.selected_movie = selected_movie

# Automatically show recommendations when a movie is selected
if st.session_state.selected_movie:
    selected_movie = st.session_state.selected_movie

    # Fetch details of the selected movie
    selected_movie_id = movies[movies['title'] == selected_movie].iloc[0].movie_id
    poster_path, title, overview = fetch_movie_details(selected_movie_id)
    
    # Display the selected movie details
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(poster_path, width=300)
    with col2:
        st.subheader('Selected Movie')
        st.write(f"**Title:** {title}")
        st.write(f"**Overview:** {overview}")
    
    # Display recommendations
    st.subheader('Recommended Movies')
    with st.spinner('Loading recommendations...'):
        recommended_movie_names, recommended_movie_posters, recommended_movie_ids = recommend(selected_movie)
    
    # Display recommendations in a grid layout
    cols = st.columns(5)
    for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
        with col:
            st.image(poster, use_column_width=True)
            st.write(name, unsafe_allow_html=True)

# Display the background image
st.markdown(
    """
    <style>
    .main {
        background: url('/mnt/data/image.png');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
