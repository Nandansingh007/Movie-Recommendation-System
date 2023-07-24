## Import Necessary Libraries
import nltk
import pickle
import pandas as pd
import numpy as np
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Load cleaned data
new_df = pd.read_csv("./Dataset/clean_df.csv")


## Model of Movie Recommendation

# Poreter Stemmer for handeling repeated words in tags feature
ps=PorterStemmer()

#Function to split the text and stemming of the text to root word
def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)

new_df["tags"] = new_df["tags"].apply(stem)

# Vectorization: Creating each movie as a Vector
cv = CountVectorizer(max_features=5000, stop_words="english")
vector = cv.fit_transform(new_df["tags"]).toarray()

# Calculating Cosine Angle between vectors
similar = cosine_similarity(vector)


"""## Saving the Model"""
pickle.dump(new_df, open("./Model/movies.pkl", "wb"))
pickle.dump(similar,open("./Model/similar.pkl","wb"))




