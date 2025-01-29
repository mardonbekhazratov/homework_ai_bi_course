from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = "flights"

try:

    flights = pd.read_parquet(current_directory / "data" / filename)

    # for i in flights.columns:
    #     print(i, end=" ")

    def pipeline(df):
        df = df[df["DepDelay"].astype(float) > 30] # Filter flights with a departure delay greater than 30 minutes.
        df["Delay_Per_Hour"] = df["DepDelay"].astype(float) / df["DepTime"].astype(float) # Add a column Delay_Per_Hour by dividing the delay by the scheduled flight duration.
        return df

    flights = flights.pipe(pipeline)
    print(flights)


except FileNotFoundError as e:
    print("File not found")

except Exception as e:
    print(e)