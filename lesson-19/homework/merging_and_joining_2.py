from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = "movie.csv"

try:
    movies = pd.read_csv(current_directory / "data" / filename)

    # print(movies.head())

    director_and_color = movies[["director_name", "color"]]
    director_and_critic = movies[["director_name", "num_critic_for_reviews"]]

    left_join = pd.merge(director_and_color, director_and_critic, on="director_name", how="left")
    outer_join = pd.merge(director_and_color, director_and_critic, on="director_name", how="outer")

    print("Number of rows after left join:", left_join.shape[0])
    print("Number of rows after full outer join:", outer_join.shape[0])

except FileNotFoundError as e:
    print("File not found")

except Exception as e:
    print(e)