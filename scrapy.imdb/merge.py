import csv
from collections import OrderedDict
import pandas as pd

df1 = pd.read_csv("movie_data.csv")
df2 = pd.read_csv("imdb_company.csv")
dfinal = df2.merge(df1, how='inner', left_on='movie_title', right_on='movie_title')
dfinal.to_csv("merged.csv", index=False)