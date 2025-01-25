from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = current_directory / "data/flights"

flights = pd.read_parquet(filename)

try:
    odc = flights[["Origin", "Dest", "Carrier"]]
except KeyError as e:
    print(e)
except:
    print("Error occured")

try:
    print("Number of unique destinations is:", len(set(flights["Dest"])))
except KeyError as e:
    print(e)
except:
    print("Error occured")