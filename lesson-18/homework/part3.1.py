from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = current_directory / "data/iris.json"

try:
    iris = pd.read_json(filename)

    numerical_columns = iris.select_dtypes("number")
    print("Mean:\n", numerical_columns.mean())
    print("---------------------------")
    print("Median:\n", numerical_columns.median())
    print("---------------------------")
    print("Standard deviation:\n", numerical_columns.std())
    print("---------------------------")

except FileNotFoundError as e:
    print("File not found")
except Exception as e:
    print(e)