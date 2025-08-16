import pandas as pd
data = pd.read_csv('top10K-TMDB-movies.csv')
data.head()

data.info()

movies = data[['id', 'title', 'overview', 'genre']]
movies.head()
movies['tags'] = movies['overview']+movies['genre']
movies.head()
new_data = movies.drop(columns=['overview','genre'])
new_data