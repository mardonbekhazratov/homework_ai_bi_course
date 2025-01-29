from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = "flights"

try:

    flights = pd.read_parquet(current_directory / "data" / filename)

    print("Total number of flights:", flights.shape[0])
    print("Average arrival delay:", flights["ArrDelay"].astype(float).mean())
    print("Maximum departure delay:", flights["DepDelay"].astype(float).max())


except FileNotFoundError as e:
    print("File not found")

except Exception as e:
    print(e)