#Importing necessary Libraries
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pickle


app = FastAPI()

#Loading the Model
similar = pickle.load(open("../Model/similar.pkl", 'rb'))
movies = pickle.load(open('../Model/movies.pkl','rb'))

# #Function to make the Recommendation
# @app.post("/recommend")
# def recommend(movie):
#     movie_index = movies[movies["title"]==movie].index[0]
#     distances = similar[movie_index]
#     movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:4]

#     for i in movie_list:
#         print(movies.iloc[i[0]].title)
#         return (movies.iloc[i[0]].title)

# Recommend top similar movies
@app.get("/recommend/")
def recommend(movie):
    # Convert the input movie name to lowercase
    movie = movie.lower()

    # Find the movie index in the movies DataFrame (and making case-insensitive comparison)
    movie_index = movies[movies["title"].str.lower() == movie].index
    
    #condition for checking the movie in the database
    if len(movie_index) == 0:
        return (f"Movie '{movie}' is not found in the database.")
        
    else:
        movie_index = movie_index[0]
        distances = similar[movie_index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:4]

        recommended_movies = [movies.iloc[i[0]].title for i in movie_list]
        return {"input_movie": movie, "recommended_movies": recommended_movies}

if __name__=="__main__":
    uvicorn.run("app:app",host="localhost", port=8084, reload=True)
    

