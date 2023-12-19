# Final 

# load the libraries
import pandas as pd 
import numpy as np 
import regex as re 
import matplotlib.pyplot as plt 

# loads the data
df = pd.read_csv('final/movie_data.csv')

# uses regex to search for the pattern 'comedy' in the dataset
pattern = r'\b[Cc]omedy\b'

# converts the rating column to a numeric value so calculations can be made
df["Rating"] = pd.to_numeric(df["Rating"], errors='coerce')

# filters the comedy movies in the dataset
comedy_movies = df[df['Genre'].str.contains(pattern, flags=re.IGNORECASE, na=False)]

# uses a loop to get a minimum rating from the user in the command line
# if a value that is not accepted is entered, it is automatically set to 4
while True:
    try:
        min_rating = int(input("Enter the minimum rating to filter the comedy movies: "))
        break
    except ValueError:
        print("Invalid input, please enter in a whole number.")
        min_rating = 4
        print("The minimum rating has been automatically set to 4.")

# filters the movies based on user input minimum rating
filtered_movies = comedy_movies[comedy_movies["Rating"] >= min_rating]

# calculates the mean of the filtered ratings by the user input value
filtered_mean_rating = np.mean(filtered_movies["Rating"])

# displays a list of the filtered movies by the user's minimum rating 
print(f"\nFiltered Comedy Movies with Rating >= {min_rating}")
print(filtered_movies[["Title", "Rating"]])

# creates and displays a histogram of all the ratings for comedy movies
plt.hist(comedy_movies["Rating"])
plt.title(f"Average Rating for Comedy Movies")
plt.xlabel("Rating")
plt.ylabel("Number of Movies")
plt.show()

# displays the mean rating for the filtered movies by user input for minimum rating
print(f"\nMean Rating: {filtered_mean_rating}")

