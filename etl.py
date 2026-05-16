import pandas as pd
import numpy as np


df_rental = pd.read_csv('rental.csv')
df_film = pd.read_csv('film.csv')
df_category = pd.read_csv('category.csv')
df_film_cat = pd.read_csv('film_category.csv')


df_merged_film = pd.merge(df_film, df_film_cat, on='film_id', how='left')
dim_film = pd.merge(df_merged_film, df_category, on='category_id', how='left')


df_rental['rental_date'] = pd.to_datetime(df_rental['rental_date'])
df_rental['return_date'] = pd.to_datetime(df_rental['return_date'])


df_rental['actual_duration'] = (df_rental['return_date'] - df_rental['rental_date']).dt.days


df_rental = pd.merge(df_rental, df_film[['film_id', 'rental_duration']], on='film_id', how='left')


df_rental['is_late'] = df_rental['actual_duration'] > df_rental['rental_duration']
df_rental['is_late'] = df_rental['is_late'].fillna(False)


dim_film['film_sk'] = np.arange(len(dim_film)) + 1
