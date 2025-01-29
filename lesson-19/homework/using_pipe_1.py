from pathlib import Path
import pandas as pd

current_directory = Path(__file__).resolve().parent

filename = "titanic.xlsx"

try:
    titanic = pd.read_excel(current_directory / "data" / filename)

    # print(titanic.head())
    print(type(titanic))
    
    def pipeline(df):
        df = df[df['Survived'] == 1] # Filter passengers who survived.
        df["Age"].fillna(df["Age"].mean(), inplace=True) # Fill missing Age values with the mean.
        df["Fare_Per_Age"] = df["Fare"] / df["Age"] # Create a new column, Fare_Per_Age, by dividing Fare by Age.
        return df
    
    titanic = titanic.pipe(pipeline)
    
    print(titanic)


except FileNotFoundError as e:
    print("File not found")

except Exception as e:
    print(e)