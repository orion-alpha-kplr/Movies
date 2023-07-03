import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

links_df = pd.read_csv('/workspaces/Movies/Data/links.csv')
movies_df = pd.read_csv('/workspaces/Movies/Data/movies.csv')
ratings_df = pd.read_csv('/workspaces/Movies/Data/ratings.csv')
tags_df = pd.read_csv('/workspaces/Movies/Data/tags.csv')


"""print(links_df.head())
print(movies_df.info())"""

high_rated_movies = ratings_df[ratings_df['rating'] >= 4.0]  # Filtrer les films bien notés
print(high_rated_movies.head())

