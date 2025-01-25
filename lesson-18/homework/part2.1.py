from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = current_directory / "data/iris.json"

try:
    iris = pd.read_json(filename)

    print("Before:", iris.columns)
    iris.columns = [column.lower() for column in iris.columns]
    print("After:", iris.columns)

    lenth_and_width = iris[["sepallength", "sepalwidth"]]
    print(lenth_and_width)

except FileNotFoundError as e:
    print("File not found")

except KeyError as e:
    print(e)
    
except:
    print("Error occured")