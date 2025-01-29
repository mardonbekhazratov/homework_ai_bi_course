from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = "titanic.xlsx"

try:
    titanic = pd.read_excel(current_directory / "data" / filename)

    # print(titanic.head())

    grouped_by_pclass = titanic.groupby("Pclass")

    dataframe = pd.DataFrame()
    print("Average age:")
    dataframe["averageAge"] = grouped_by_pclass["Age"].mean()
    print(dataframe["averageAge"])

    print("Total fare:")
    dataframe["totalFare"] = grouped_by_pclass["Fare"].sum()
    print(dataframe["totalFare"])

    print("Count of passengers:")
    dataframe["countOfPassengers"] = grouped_by_pclass["PassengerId"].count()
    print(dataframe["countOfPassengers"])

    print(dataframe)


except FileNotFoundError as e:
    print("File not found")

except Exception as e:
    print(e)