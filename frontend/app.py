import streamlit as st
import requests
import pickle

#import movies model
movies = pickle.load(open('./movies.pkl','rb'))

#port where backend is running
api_base_url = "http://backend:8000"

#Header Display
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'Type or Select Movie From Dropdown',
movies['title'].values
)

if st.button("Recommend"):
    
    # Prepare the API endpoint and parameters
    api_endpoint = f"{api_base_url}/recommend/"
    params = {"movie": selected_movie_name}

    # Make the API call to get the recommendations
    response = requests.get(api_endpoint, params=params)

    if response.status_code == 200:
        
        # Successfully received the response from the API
        data = response.json()
        input_movie = data["input_movie"]
        recommended_movies = data["recommended_movies"]

        # Display the recommendation results
        st.write(f"Input Movie: {input_movie}")
        st.write("Recommended Movies:")
        for movie in recommended_movies:
            st.write(movie)
    else:
        # Something went wrong with the API call
        st.error("Error occurred while fetching recommendations. Please try again.")

