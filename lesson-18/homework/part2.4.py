from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = current_directory / "data/movie.csv"

try:
    movies = pd.read_csv(filename)

    filtered = movies[movies["duration"] > 120]
    print(filtered)
    
    filtered.sort_values(by="director_facebook_likes", inplace=True)
    print("Movies sorted by director_facebook_likes:\n", filtered)
except FileNotFoundError as e:
    print("File not found")
except:
    print("Error occured")