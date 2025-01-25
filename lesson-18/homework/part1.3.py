from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = current_directory / "data/titanic.xlsx"

try:
    titanic = pd.read_excel(filename)

    print(titanic.head(5))
except FileNotFoundError as e:
    print("File not found")
except:
    print("Error occured")