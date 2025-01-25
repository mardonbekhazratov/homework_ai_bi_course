from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = current_directory / "data/flights"

try:
    flights = pd.read_parquet(filename)

    for column in flights.select_dtypes("number").columns:
        flights[flights[column].isna()] = flights[column].mean()
    
    print(flights)
except FileNotFoundError as e:
    print("File not found")
except Exception as e:
    print(e)
