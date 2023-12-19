# Final 


# using advanced topics git, pandas, reg exp
import pandas as pd 
import numpy as np 
import regex as re
import matplotlib.pyplot as plt 

df = pd.read_csv('movie_data.csv')
print(df)

pattern = r'\bcomedy\b'

def filter_plot(df, genre_pattern): 

    comedy_movies = df[df['Genre'].str.contains(genre_pattern, flags=re.IGNORECASE, na=False)]
    print(comedy_movies)

    print(f"{genre_pattern.capitalize()}")

    try:
        min_rating = float(input("Enter the minimum rating to filter the comedy movies: "))
    except ValueError:
        print("Invalid input, please enter in a valid numeric value.")
        min_rating = np.nan # placeholder for an invalid input 

    filtered_movies = np

    mean_rating_comedy = np.mean(pd.to_numeric(comedy_movies['Rating'], errors='coerce'))
    print(f"\nThe comedy movies with a rating that is greater than or equal to {min_rating}: ")

i think this 
