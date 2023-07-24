#importing Libraries
import pandas as pd
import numpy as np
import ast


#Data Loading
movies = pd.read_csv("./Dataset/tmdb_5000_movies.csv")
credits = pd.read_csv("./Dataset/tmdb_5000_credits.csv")

# Data Cleaning
df = movies.merge(credits, on="title")

df.head(1)

#selecting particular column
df=df[["movie_id","title","overview","genres","keywords","cast","crew"]]
df.head(1)

#checking null value
df.isnull().sum()

#dropping null value
df.dropna(inplace=True)

df.head(1)

df['genres'][0]


def convert(obj):
    '''
    # Extracting Genres from json format
    # Getting Genres["name"] from this function
    '''
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i["name"])
    return L

df["genres"] = df["genres"].apply(convert)

df.head(1)

df['keywords'][0]

df["keywords"] = df["keywords"].apply(convert)


def convert2(obj):
    '''
    # Getting characters from the json File
    # Getting Top 3 charecters in cast feature from this function
    '''
    L=[]
    counter = 0
    for i in ast.literal_eval(obj):
        if counter!=3:
            L.append(i["name"])
            counter+=1
        else:
            break
    return L

df["cast"] = df["cast"].apply(convert2)

df.head(1)


def fetch(obj):
    '''
    # Getting Crew["Director"] names from this function
    '''
    L =[]
    for i in ast.literal_eval(obj):
        if i["job"] == "Director":
            L.append(i["name"])
            break
    return L

df["crew"] = df["crew"].apply(fetch)

df.head(1)

df["overview"] = df["overview"].apply(lambda x:x.split())

# Removing " " (spaces) between Words from features
df["cast"] = df["cast"].apply(lambda x:[i.replace(" ","") for i in x])
df["crew"] = df["crew"].apply(lambda x:[i.replace(" ","") for i in x])
df["keywords"] = df["keywords"].apply(lambda x:[i.replace(" ","") for i in x])
df["genres"] = df["genres"].apply(lambda x:[i.replace(" ","") for i in x])

df.head(1)

#creating tags colums
df["tags"] = df["overview"] + df["genres"] + df["keywords"] + df["cast"] + df["crew"]

# cleaned data is ready now!!!
clean_df = df[["movie_id", "title", "tags"]]

# clean_df["tags"] = clean_df["tags"].apply(lambda x:" ".join(x))
clean_df.loc[:, "tags"] = clean_df["tags"].apply(lambda x: " ".join(x))
# clean_df["tags"] = clean_df["tags"].apply(lambda x:x.lower())
clean_df.loc[:, "tags"] = clean_df["tags"].apply(lambda x: x.lower())

# Save the DataFrame to the CSV file
clean_df.to_csv("./Dataset/clean_df.csv", index=False)