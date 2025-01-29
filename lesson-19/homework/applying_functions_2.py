from pathlib import Path
import pandas as pd
import sqlite3
import numpy as np

current_directory = Path(__file__).resolve().parent

filename = "chinook.db"

try:
    with sqlite3.connect(current_directory / "data" / filename) as connection:
        employees = pd.read_sql("SELECT * FROM employees", con=connection)

    # print(employees.columns)
    employees["Salary"] = np.random.randint(50000, 100000, employees.shape[0])

    # Normalize salaries within each department (ReportsTo group)
    def normalize_salaries(group):
        max_salary = group.max()
        min_salary = group.min()
        return (group - min_salary) / (max_salary - min_salary) if max_salary != min_salary else group

    employees["Normalized_Salary"] = (
        employees
            .groupby("ReportsTo")["Salary"]
            .transform(normalize_salaries)
    )

    print(employees[["FirstName", "LastName", "ReportsTo", "Salary", "Normalized_Salary"]])

except FileNotFoundError as e:
    print("File not found")

except Exception as e:
    print(e)