from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = current_directory / "data/flights"

try:
    flights = pd.read_parquet(filename)

    print(flights.info())
except FileNotFoundError as e:
    print("File not found")
except:
    print("Error occured")
