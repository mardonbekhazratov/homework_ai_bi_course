from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = "movie.csv"

try:
    
    movies = pd.read_csv(current_directory / "data" / filename)

    # print(movies.head())

    def classify_duration(group):
        if group["duration"]<60:
            return "Short"
        if group["duration"]<120:
            return "Medium"
        return "Long"

    movies["length"] = movies.apply(classify_duration, axis=1)
    print(movies.head())

except FileNotFoundError as e:
    print("File not found")

except Exception as e:
    print(e)