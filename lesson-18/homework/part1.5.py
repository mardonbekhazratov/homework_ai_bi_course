from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = current_directory / "data/movie.csv"

try:
    movies = pd.read_csv(filename)

    print(movies.sample(10))
except FileNotFoundError as e:
    print("File not found")
except ValueError as e:
    print(e)
except:
    print("Error occured")