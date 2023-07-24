#import necessary modules
import pickle
import pandas as pd

#loading picke model
similar = pickle.load(open("./Model/similar.pkl", 'rb'))
movies = pickle.load(open('./model/movies.pkl','rb'))


# Creating our Recommend function it will return Top 3 movies back
# Recommend top similar movies
# def recommend(movie):
    
#     movie_index = movies[movies["title"]==movie].index[0]
#     distances = similar[movie_index]
#     movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:4]

#     for i in movie_list:
#         print (movies.iloc[i[0]].title)

"""## Testing the result Results"""
# recommend("Batman")

def recommend(movie):
    # Convert the input movie name to lowercase
    movie = movie.lower()

    # Find the movie index in the movies DataFrame (case-insensitive comparison)
    movie_index = movies[movies["title"].str.lower() == movie].index
    
    #condition for checking the movie in the database
    if len(movie_index) == 0:
        print(f"Movie '{movie}' not found in the database.")
        
    else:
        movie_index = movie_index[0]
        distances = similar[movie_index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:4]

        recommended_movies = [movies.iloc[i[0]].title for i in movie_list]
        print (recommended_movies)

"""## Testing the result Results"""
recommend("Oppenheimer")










