from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = current_directory / "data/movie.csv"

try:
    movies = pd.read_csv(filename)

    sorted_by_likes = movies.sort_values(by="director_facebook_likes", ascending=False)
    print(sorted_by_likes.head(1))

    sorted_by_duration = movies.sort_values(by="duration", ascending=False)
    print(sorted_by_duration.head(5))

except FileNotFoundError as e:
    print("File not found")
except Exception as e:
    print(e)