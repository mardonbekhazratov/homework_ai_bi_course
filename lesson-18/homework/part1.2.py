from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = current_directory / "data/iris.json"

try:
    iris = pd.read_json(filename)

    print(iris.shape)
    print(iris.columns)

except FileNotFoundError as e:
    print("File not found")
except:
    print("Error occured")