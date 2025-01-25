from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = current_directory / "data/titanic.xlsx"

try:
    titanic = pd.read_excel(filename)
    
    ages = titanic["Age"]
    print("Minimum:", ages.min())
    print("Maximum:", ages.max())
    print("Sum:", ages.sum())
    
except FileNotFoundError as e:
    print("File not found")
except KeyError as e:
    print(e)
except Exception as e:
    print(e)
