# Final 

# using advanced topics git, pandas, reg exp
import pandas as pd 
import numpy as np 
import regex as re 
import matplotlib.pyplot as plt 

df = pd.read_csv('movie_data.csv')
print(df)

pattern = r'\b[Cc]omedy\b'

comedy_movies = df[df['Genre'].str.contains(pattern, flags=re.IGNORECASE, na=False)]
print("Here are all of the comedy movies:")
print(comedy_movies[["Title", "Rating"]]) 

try:
    min_rating = int(input("Enter the minimum rating to filter the comedy movies: "))
except ValueError:
    print("Invalid input, please enter in a valid numeric value.")
    min_rating = 4.1 

df["Rating"] = pd.to_numeric(df["Rating"], errors='coerce')

filtered_movies = comedy_movies[comedy_movies["Rating"] >= {min_rating}]

min_rating = 7 

print(f"\nFiltered Comedy Movies with Rating >= {min_rating}")
print(filtered_movies[["Title", "Rating"]])
