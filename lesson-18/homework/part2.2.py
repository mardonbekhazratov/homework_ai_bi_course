from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = current_directory / "data/titanic.xlsx"

try:
    titanic = pd.read_excel(filename)
    
    above30 = titanic[titanic["Age"]>30]
    print(above30)
except FileNotFoundError as e:
    print("File not found")
except KeyError as e:
    print(e)
except:
    print("Error occured")
