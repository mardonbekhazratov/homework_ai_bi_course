from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = "movie.csv"

try:
    
    movies = pd.read_csv(current_directory / "data" / filename)


    grouped_by_color = movies.groupby("color")
    grouped_by_director = movies.groupby("director_name")

    print("Total num critic for reviews:\n")
    print("Groupped by color:")
    print(grouped_by_color["num_critic_for_reviews"].sum())
    print()

    print("Groupped by director name:")
    print(grouped_by_director["num_critic_for_reviews"].sum())
    print("\n")

    print("Average duration:\n")
    print("Groupped by color:")
    print(grouped_by_color["duration"].mean())
    print()

    print("Groupped by director name:")
    print(grouped_by_director["duration"].mean())
    print()

except FileNotFoundError as e:
    print("File not found")

except Exception as e:
    print(e)