from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = "titanic.xlsx"

def classify_age_group(x):
    return "Child" if x["Age"] < 18 else "Adult"

try:
    titanic = pd.read_excel(current_directory / "data" / filename)

    # print(titanic.columns)

    titanic["Age_Group"] = titanic.apply(classify_age_group, axis=1)

    print(titanic)


except FileNotFoundError as e:
    print("File not found")

except Exception as e:
    print(e)