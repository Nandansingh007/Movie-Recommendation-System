#import necessary modules
import pickle
import pandas as pd

#loading picke model
similar = pickle.load(open("./Model/similar.pkl", 'rb'))
movies = pickle.load(open('./model/movies.pkl','rb'))


# Creating our Recommend function it will return Top 3 movies back
# Recommend top similar movies
def recommend(movie):
    movie_index = movies[movies["title"]==movie].index[0]
    distances = similar[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:4]

    for i in movie_list:
        print(movies.iloc[i[0]].title)

"""## Testing the result Results"""
recommend("Batman Begins")





